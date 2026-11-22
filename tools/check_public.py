#!/usr/bin/env python3
"""Offline checks for the public showcase, using only Python's standard library.

This is a release hygiene check, not a security audit or a trading-engine test.
It cannot decide whether an apparently harmless sentence reveals private logic.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, field
from html.parser import HTMLParser
import io
import ipaddress
import json
import math
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import tempfile
import tokenize
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


MANIFEST = "public-files.txt"
MAX_FILE_BYTES = 5 * 1024 * 1024
TEXT_SUFFIXES = {".md", ".txt", ".json", ".svg", ".py", ".yml", ".yaml", ".html"}
TEXT_NAMES = {"LICENSE", ".gitignore", ".gitattributes"}
ARCHIVE_SUFFIXES = {".zip", ".tar", ".tgz", ".gz", ".bz2", ".xz", ".7z", ".rar", ".jar", ".whl"}
ARCHIVE_MAGIC = (
    bytes.fromhex("504b0304"), bytes.fromhex("504b0506"),
    bytes.fromhex("504b0708"), bytes.fromhex("1f8b"),
    bytes.fromhex("377abcaf271c"), bytes.fromhex("526172211a07"),
    bytes.fromhex("fd377a585a00"), b"BZh",
)
SVG_NS = "http://www.w3.org/2000/svg"
XML_NS = "http://www.w3.org/XML/1998/namespace"
XLINK_NS = "http://www.w3.org/1999/xlink"

# Patterns are deliberately expressed without embedding a real credential.
# Findings report only the rule and location, never the matched value.
SECRET_RULES = (
    ("private-key header", re.compile(r"-{5}BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-{5}")),
    ("cloud access-key format", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub token format", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})\b")),
    ("service secret-key format", re.compile(r"\bsk-(?:proj-|svcacct-|live_)?[A-Za-z0-9_-]{24,}\b")),
    ("Slack token format", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("JWT-like credential", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{16,}\b")),
    ("credential assignment", re.compile(
        r"(?im)\b(?:api[_-]?key|api[_-]?secret|private[_-]?key|access[_-]?token|auth[_-]?token|password|passwd|secret)"
        r"\b[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_+/=.-]{16,}"
    )),
    ("URL with embedded credentials", re.compile(r"(?i)https?://[^/\s:@]+:[^/\s@]+@")),
    ("hexadecimal wallet address", re.compile(r"(?i)\b0x[0-9a-f]{40}\b")),
    ("bech32-style wallet address", re.compile(r"(?i)\bbc1[ac-hj-np-z02-9]{25,87}\b")),
    ("email/contact address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("absolute operational path", re.compile(r"/(?:home|root|Users|etc|var|srv|opt|mnt|workspace)/(?:[^\s\"'<>)]*)")),
    ("Windows operational path", re.compile(r"(?i)\b[A-Z]:\\(?:Users|ProgramData|Windows|Temp)\\[^\s\"'<>]*")),
    ("home-relative operational path", re.compile(r"\x7e/(?:[^\s\"'<>)]*)")),
)
IP_CANDIDATES = (
    re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])"),
    re.compile(r"(?<![\w:])(?:[0-9A-Fa-f]{0,4}:){2,7}[0-9A-Fa-f]{0,4}(?![\w:])"),
)
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\")\s]+)['\"]?\s*\)", re.IGNORECASE)
REMOTE_VALUE = re.compile(r"(?i)(?:https?:|ftp:|file:|data:|javascript:|vbscript:|//)")


@dataclass
class ValidationResult:
    files: dict[str, bytes] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def read_manifest(root: Path, errors: list[str]) -> set[str]:
    manifest = root / MANIFEST
    if manifest.is_symlink() or not manifest.is_file():
        errors.append(f"{MANIFEST}: expected a regular allowlist file")
        return set()
    try:
        content = manifest.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{MANIFEST}: cannot read UTF-8 allowlist ({type(exc).__name__})")
        return set()
    paths: set[str] = set()
    portable_names: set[str] = set()
    prefix_spellings: dict[str, str] = {}
    reserved = {"CON", "PRN", "AUX", "NUL"}
    reserved.update(f"{prefix}{n}" for prefix in ("COM", "LPT") for n in range(1, 10))
    for number, raw in enumerate(content.splitlines(), 1):
        name = raw.strip()
        if not name or name.startswith("#"):
            continue
        parts = name.split("/")
        valid = (
            raw == name
            and re.fullmatch(r"[A-Za-z0-9_./-]+", name) is not None
            and not name.startswith("/")
            and all(part.casefold() not in {"", ".", "..", ".git", "__pycache__"} for part in parts)
            and all(not part.endswith(".") for part in parts)
            and all(part.split(".")[0].upper() not in reserved for part in parts)
        )
        if not valid:
            errors.append(f"{MANIFEST}:{number}: noncanonical or unsafe relative path")
            continue
        if name.casefold() in portable_names:
            errors.append(f"{MANIFEST}:{number}: duplicate or case-colliding path")
            continue
        prefixes = ["/".join(parts[:index]) for index in range(1, len(parts) + 1)]
        if any(prefix_spellings.get(prefix.casefold(), prefix) != prefix for prefix in prefixes):
            errors.append(f"{MANIFEST}:{number}: path-prefix case collision")
            continue
        paths.add(name)
        portable_names.add(name.casefold())
        prefix_spellings.update((prefix.casefold(), prefix) for prefix in prefixes)
    if MANIFEST not in paths:
        errors.append(f"{MANIFEST}: the allowlist must include itself")
    return paths


def cache_is_bytecode_only(directory: Path, relative: str, allowed: set[str]) -> bool:
    """Only normal Python cache files belonging to allowlisted source are ignored."""
    owner = PurePosixPath(relative).parent
    for child in directory.iterdir():
        if child.is_symlink() or not child.is_file():
            return False
        match = re.fullmatch(r"(.+)\.(?:cpython|pypy)-\d+(?:\.opt-[0-2])?\.pyc", child.name)
        if not match or (owner / (match.group(1) + ".py")).as_posix() not in allowed:
            return False
    return True


def collect_files(root: Path, allowed: set[str], package_tree: bool, result: ValidationResult) -> None:
    directories = {"."}
    for name in allowed:
        directories.update(parent.as_posix() for parent in PurePosixPath(name).parents)

    def walk(directory: Path, prefix: str = "") -> None:
        try:
            entries = sorted(os.scandir(directory), key=lambda entry: entry.name)
        except OSError as exc:
            result.errors.append(f"{prefix or '.'}: cannot inspect directory ({type(exc).__name__})")
            return
        for entry in entries:
            name = f"{prefix}/{entry.name}" if prefix else entry.name
            path = Path(entry.path)
            if entry.is_symlink():
                result.errors.append(f"{name}: symbolic links are forbidden")
                continue
            if name == ".git" and not package_tree and entry.is_dir(follow_symlinks=False):
                continue
            if entry.name == ".git":
                result.errors.append(f"{name}: Git metadata is forbidden here")
                continue
            if entry.is_dir(follow_symlinks=False):
                if entry.name == "__pycache__":
                    try:
                        ignorable = not package_tree and cache_is_bytecode_only(path, name, allowed)
                    except OSError:
                        ignorable = False
                    if not ignorable:
                        result.errors.append(f"{name}: only generated bytecode caches are ignored in repository mode")
                    continue
                if name not in directories:
                    result.errors.append(f"{name}: directory is outside the public allowlist")
                walk(path, name)
                continue
            if not entry.is_file(follow_symlinks=False):
                result.errors.append(f"{name}: expected a regular file")
                continue
            if name not in allowed:
                result.errors.append(f"{name}: file is outside the public allowlist")
                continue
            try:
                if entry.stat(follow_symlinks=False).st_size > MAX_FILE_BYTES:
                    result.errors.append(f"{name}: exceeds the public text-file size limit")
                    continue
                result.files[name] = path.read_bytes()
            except OSError as exc:
                result.errors.append(f"{name}: cannot read file ({type(exc).__name__})")

    walk(root)
    for name in sorted(allowed - result.files.keys()):
        result.errors.append(f"{name}: allowlisted file is missing or unreadable")


def ip_scan_content(name: str, text: str) -> str:
    """Python syntax colons are not IPv6; strings and comments remain scanned."""
    if PurePosixPath(name).suffix.lower() != ".py":
        return text
    try:
        ast.parse(text)
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (SyntaxError, ValueError, RecursionError, tokenize.TokenError):
        return text
    starts = [0]
    for line in text.splitlines(keepends=True):
        starts.append(starts[-1] + len(line))
    characters = list(text)
    for token in tokens:
        if token.type == tokenize.OP and token.string == ":":
            characters[starts[token.start[0] - 1] + token.start[1]] = " "
    return "".join(characters)


def inspect_text(name: str, data: bytes, errors: list[str]) -> str | None:
    path = PurePosixPath(name)
    if path.suffix.lower() in ARCHIVE_SUFFIXES or data.startswith(ARCHIVE_MAGIC) or data[257:262] == b"ustar":
        errors.append(f"{name}: nested archives are forbidden")
        return None
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
        errors.append(f"{name}: unsupported public file type; only reviewed text and SVG formats are permitted")
        return None
    try:
        text = data.decode("utf-8")
    except UnicodeError:
        errors.append(f"{name}: binary or non-UTF-8 content is forbidden")
        return None
    if any(ord(char) < 32 and char not in "\t\n\r" for char in text):
        errors.append(f"{name}: binary control characters are forbidden")
        return None
    for label, pattern in SECRET_RULES:
        for match in pattern.finditer(text):
            errors.append(f"{name}:{line_at(text, match.start())}: review required: {label}")
    ip_content = ip_scan_content(name, text)
    for pattern in IP_CANDIDATES:
        for match in pattern.finditer(ip_content):
            try:
                ipaddress.ip_address(match.group())
            except ValueError:
                continue
            errors.append(f"{name}:{line_at(text, match.start())}: literal IP address is forbidden")
    return text


def unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate object key")
        result[key] = value
    return result


def reject_json_constant(value: str) -> None:
    raise ValueError("non-finite JSON number")


def inspect_json(name: str, text: str, errors: list[str]) -> None:
    try:
        data = json.loads(text, object_pairs_hook=unique_json_object, parse_constant=reject_json_constant)
    except (ValueError, RecursionError):
        errors.append(f"{name}: invalid JSON, duplicate keys, or non-finite number")
        return
    if not isinstance(data, dict) or data.get("data_classification") != "synthetic":
        errors.append(f"{name}: JSON must be an object labelled data_classification='synthetic'")
        return
    if "display_type" in data and data["display_type"] != "illustration_only":
        errors.append(f"{name}: display_type must be 'illustration_only' when present")

    def visit(value: object) -> None:
        if isinstance(value, float) and not math.isfinite(value):
            errors.append(f"{name}: non-finite decoded JSON number is forbidden")
        elif isinstance(value, list):
            for item in value:
                visit(item)
        elif isinstance(value, dict):
            for key, item in value.items():
                if key.endswith("_id") or key.endswith("_ids"):
                    family = "SOURCE_[A-Z]" if key in {"source_id", "source_ids"} else (
                        "ASSET_[A-Z]" if key in {"asset_id", "asset_ids"} else "DEMO_[A-Z0-9_]+"
                    )
                    identifiers = item if key.endswith("_ids") and isinstance(item, list) else [item]
                    if not identifiers or any(not isinstance(identifier, str) or re.fullmatch(family, identifier) is None for identifier in identifiers):
                        errors.append(f"{name}: identifier field must use the documented fictional ID family")
                visit(item)

    visit(data)


def xml_name(tag: str) -> tuple[str, str]:
    if tag.startswith("{"):
        namespace, local = tag[1:].split("}", 1)
        return namespace, local
    return "", tag


def inspect_svg(name: str, text: str, errors: list[str]) -> set[str]:
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b", text, re.IGNORECASE):
        errors.append(f"{name}: SVG document types and entity declarations are forbidden")
        return set()
    if re.search(r"<\?(?!xml(?:\s|\?>))", text, re.IGNORECASE):
        errors.append(f"{name}: SVG processing instructions are forbidden")
        return set()
    try:
        root = ET.fromstring(text)
    except (ET.ParseError, ValueError):
        errors.append(f"{name}: invalid SVG XML")
        return set()
    if root.tag != f"{{{SVG_NS}}}svg":
        errors.append(f"{name}: expected an SVG root in the SVG namespace")
    ids: set[str] = set()
    references: list[str] = []

    def inspect_css(value: str) -> None:
        if "\\" in value or "@" in value or re.search(r"(?i)expression\s*\(|-moz-binding|behavior\s*:|(?:-webkit-)?image(?:-set)?\s*\(|\bsrc\s*\(", value):
            errors.append(f"{name}: active, imported, escaped, or unsupported SVG CSS is forbidden")
        if REMOTE_VALUE.search(value):
            errors.append(f"{name}: external or embedded SVG resources are forbidden")
        url_matches = list(CSS_URL.finditer(value))
        if len(url_matches) != len(re.findall(r"url\s*\(", value, re.IGNORECASE)):
            errors.append(f"{name}: unrecognized SVG CSS URL syntax")
        for match in url_matches:
            target = match.group(1)
            if not target.startswith("#"):
                errors.append(f"{name}: SVG CSS URLs must refer to an internal ID")
            else:
                references.append(target[1:])

    for node in root.iter():
        namespace, local = xml_name(node.tag)
        if namespace != SVG_NS:
            errors.append(f"{name}: foreign XML elements are forbidden in SVG")
        if local.lower() in {"script", "foreignobject", "iframe", "object", "embed", "image", "audio", "video", "animate", "animatemotion", "animatetransform", "set"}:
            errors.append(f"{name}: active or embedded-media SVG element is forbidden")
        identifier = node.attrib.get("id")
        if identifier:
            if identifier in ids:
                errors.append(f"{name}: duplicate SVG ID")
            ids.add(identifier)
        if local.lower() == "style":
            inspect_css("".join(node.itertext()))
        for key, value in node.attrib.items():
            attribute_ns, attribute = xml_name(key)
            if attribute_ns not in {"", SVG_NS, XML_NS, XLINK_NS}:
                errors.append(f"{name}: foreign XML attributes are forbidden in SVG")
            if attribute_ns == XML_NS and attribute.lower() == "base":
                errors.append(f"{name}: SVG must not override the resource base URL")
            if attribute.lower().startswith("on"):
                errors.append(f"{name}: SVG event-handler attributes are forbidden")
            if attribute.lower() == "href":
                target = value.strip()
                if not target.startswith("#") or len(target) == 1:
                    errors.append(f"{name}: SVG href must refer to an internal ID")
                else:
                    references.append(target[1:])
            if attribute.lower() == "aria-labelledby":
                references.extend(value.split())
            inspect_css(value)
    for identifier in references:
        if identifier not in ids:
            errors.append(f"{name}: SVG refers to a missing internal ID")
    return ids


def mask_markdown_code(text: str, *, inline: bool = True) -> str:
    """Keep line breaks while removing common fenced and inline code forms."""
    lines: list[str] = []
    fence_char = ""
    fence_size = 0
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence_char:
            if match and match.group(1)[0] == fence_char and len(match.group(1)) >= fence_size:
                fence_char = ""
            lines.append("\n" if line.endswith("\n") else "")
        elif match:
            fence_char, fence_size = match.group(1)[0], len(match.group(1))
            lines.append("\n" if line.endswith("\n") else "")
        else:
            lines.append(line)
    content = "".join(lines)
    return re.sub(r"(`+)([^`\n]*?)\1", lambda match: " " * len(match.group()), content) if inline else content


class MarkupLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is None:
                continue
            if key == "id" or (tag == "a" and key == "name"):
                self.ids.add(value)
            if key in {"href", "src", "poster"}:
                self.links.append((value, self.getpos()[0]))
            if key == "srcset":
                self.links.extend((candidate.strip().split()[0], self.getpos()[0]) for candidate in value.split(",") if candidate.strip())
            if key == "style":
                self.links.extend((match.group(1), self.getpos()[0]) for match in CSS_URL.finditer(value))

    handle_startendtag = handle_starttag


def markdown_heading_ids(text: str) -> set[str]:
    ids: set[str] = set()
    for match in re.finditer(r"(?m)^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$|^([^\n]+)\n {0,3}(?:=+|-+)\s*$", text):
        heading = match.group(1) or match.group(2)
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"!?\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        candidate, number = slug, 0
        while candidate in ids:
            number += 1
            candidate = f"{slug}-{number}"
        ids.add(candidate)
    return ids


def collect_markup(name: str, text: str, errors: list[str]) -> tuple[set[str], list[tuple[str, int]]]:
    markdown = PurePosixPath(name).suffix.lower() == ".md"
    content = mask_markdown_code(text) if markdown else text
    parser = MarkupLinks()
    try:
        parser.feed(content)
    except (ValueError, AssertionError):
        errors.append(f"{name}: unable to parse HTML link attributes")
    ids, links = parser.ids, parser.links
    if not markdown:
        links.extend((match.group(1), line_at(content, match.start())) for match in CSS_URL.finditer(content))
        return ids, links
    ids.update(markdown_heading_ids(mask_markdown_code(text, inline=False)))
    inline_link = re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+['\"][^\n]*?['\"])?\s*\)")
    for match in inline_link.finditer(content):
        links.append((match.group(1) or match.group(2), line_at(content, match.start())))
    definitions: dict[str, str] = {}
    for match in re.finditer(r"(?m)^ {0,3}\[([^\]\n]+)\]:\s*(?:<([^>\n]+)>|(\S+))", content):
        label = " ".join(match.group(1).lower().split())
        target = match.group(2) or match.group(3)
        definitions[label] = target
        links.append((target, line_at(content, match.start())))
    for match in re.finditer(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]", content):
        label = " ".join((match.group(2) or match.group(1)).lower().split())
        if label not in definitions:
            errors.append(f"{name}:{line_at(content, match.start())}: undefined Markdown reference link")
    return ids, links


def inspect_link(name: str, target: str, number: int, files: dict[str, bytes], anchors: dict[str, set[str]], errors: list[str]) -> None:
    location = f"{name}:{number}"
    try:
        url = urlsplit(target)
    except ValueError:
        errors.append(f"{location}: malformed link")
        return
    if url.scheme:
        if url.scheme.lower() not in {"https", "http", "mailto"}:
            errors.append(f"{location}: unsupported link scheme")
        return
    if url.netloc:
        errors.append(f"{location}: use an explicit scheme for an external link")
        return
    path = unquote(url.path)
    if path.startswith("/") or "\\" in path or "\x00" in path:
        errors.append(f"{location}: use a portable repository-relative link")
        return
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
    if resolved == ".." or resolved.startswith("../"):
        errors.append(f"{location}: relative link escapes the repository")
        return
    if resolved not in files:
        prefix = "" if resolved == "." else resolved.rstrip("/") + "/"
        if any(filename.startswith(prefix) for filename in files):
            readme = prefix + "README.md"
            if url.fragment and readme not in files:
                errors.append(f"{location}: directory link has no README for its fragment")
                return
            resolved = readme
        else:
            errors.append(f"{location}: relative link target is missing or outside the allowlist")
            return
    if url.fragment:
        if resolved not in anchors:
            errors.append(f"{location}: fragment target is not a Markdown, HTML, or SVG document")
        elif unquote(url.fragment) not in anchors[resolved]:
            errors.append(f"{location}: fragment does not match a document heading or element ID")


def validate_tree(root: Path, *, package_tree: bool = False) -> ValidationResult:
    result = ValidationResult()
    if root.is_symlink() or not root.is_dir():
        result.errors.append(".: repository root must be a real directory")
        return result
    allowed = read_manifest(root, result.errors)
    collect_files(root, allowed, package_tree, result)
    anchors: dict[str, set[str]] = {}
    links: dict[str, list[tuple[str, int]]] = {}
    for name, data in sorted(result.files.items()):
        text = inspect_text(name, data, result.errors)
        if text is None:
            continue
        suffix = PurePosixPath(name).suffix.lower()
        if suffix == ".json":
            inspect_json(name, text, result.errors)
        elif suffix == ".svg":
            anchors[name] = inspect_svg(name, text, result.errors)
        elif suffix in {".md", ".html"}:
            anchors[name], links[name] = collect_markup(name, text, result.errors)
    for name, document_links in links.items():
        for target, number in document_links:
            inspect_link(name, target, number, result.files, anchors, result.errors)
    result.errors = sorted(set(result.errors))
    return result


def run_self_test() -> int:
    """Small adversarial fixtures cover release failures independently of the repo."""
    checks = 0
    with tempfile.TemporaryDirectory(prefix="public-showcase-check-") as directory:
        root = Path(directory)
        base = {
            "README.md": "# Public example\n\n[Details](docs/note.md#details)\n\n[Code heading](docs/note.md#run-checkpy)\n\n![Drawing](assets/demo.svg)\n",
            "docs/note.md": "# Details\n\nSynthetic example only.\n\n## Run `check.py`\n",
            "assets/demo.svg": f'<svg xmlns="{SVG_NS}" viewBox="0 0 10 10"><title id="title">Demo</title><rect width="10" height="10"/></svg>\n',
            "examples/demo.json": json.dumps({"data_classification": "synthetic", "source_id": "SOURCE_A", "asset_id": "ASSET_X", "example_id": "DEMO_CHECK"}),
            "tools/demo.py": "# Public helper\n",
        }

        def install(changes: dict[str, str | bytes] | None = None) -> None:
            for child in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
                if child.is_symlink() or child.is_file():
                    child.unlink()
                else:
                    child.rmdir()
            files = dict(base)
            files.update(changes or {})
            files[MANIFEST] = "\n".join(sorted([*files, MANIFEST])) + "\n"
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))

        def expect(label: str, needle: str | None, *, package_tree: bool = False) -> None:
            nonlocal checks
            errors = validate_tree(root, package_tree=package_tree).errors
            correct = not errors if needle is None else any(needle in error for error in errors)
            if not correct:
                raise AssertionError(f"self-test failed: {label}")
            checks += 1

        install()
        expect("valid minimal showcase", None)
        expect("valid package tree", None, package_tree=True)
        install({"README.md": "[Missing](absent.md)\n"})
        expect("broken relative link", "relative link target")
        install({"README.md": "[Missing](docs/note.md#absent)\n"})
        expect("broken fragment", "fragment does not match")
        install()
        (root / "unlisted.txt").write_text("Unexpected file", encoding="utf-8")
        expect("unlisted file", "outside the public allowlist")
        install({"Docs/a.txt": "A", "docs/b.txt": "B"})
        expect("case-colliding directory prefixes", "path-prefix case collision")
        install({".Git/config.txt": "Synthetic metadata fixture"})
        expect("casefolded Git metadata path", "unsafe relative path")
        install({"tools/demo.py": "items = values[" + ":" * 2 + "2]\n"})
        expect("Python slicing is not an IPv6 literal", None)
        install({"tools/demo.py": 'address = "' + ":" * 2 + '2"\n'})
        expect("Python string IP is still detected", "literal IP address")
        install({"notes.txt": "gh" + "p_" + "a" * 36})
        expect("token detector", "GitHub token format")
        install({"notes.txt": "0" + "x" + "a" * 40})
        expect("wallet detector", "wallet address")
        install({"notes.txt": ".".join(("192", "0", "2", "10"))})
        expect("IP detector", "literal IP address")
        install({"notes.txt": "/" + "home" + "/demo/runtime.env"})
        expect("private path detector", "absolute operational path")
        install({"assets/demo.svg": f'<svg xmlns="{SVG_NS}"><script/></svg>'})
        expect("active SVG", "active or embedded-media")
        install({"assets/demo.svg": f'<svg xmlns="{SVG_NS}"><use href="https://example.invalid/demo.svg"/></svg>'})
        expect("external SVG", "SVG href")
        install({"assets/demo.svg": f'<?xml-stylesheet href="remote.css"?><svg xmlns="{SVG_NS}"/>'})
        expect("SVG processing instruction", "processing instructions")
        install({"assets/demo.svg": f'<svg xmlns="{SVG_NS}" xml:base="other/"><g id="x"/><use href="#x"/></svg>'})
        expect("SVG relative base override", "resource base URL")
        install({"assets/demo.svg": f'<svg xmlns="{SVG_NS}"><g style=\'background-image:image-set("//example.invalid/a.png" 1x)\'/></svg>'})
        expect("SVG alternate CSS image function", "unsupported SVG CSS")
        install({"examples/demo.json": '{"data_classification":"real"}'})
        expect("non-synthetic JSON", "data_classification")
        install({"examples/demo.json": '{"data_classification":"synthetic","source_id":"ACTUAL"}'})
        expect("nonfictional ID", "fictional ID family")
        install({"examples/demo.json": '{"data_classification":"synthetic","x":1,"x":2}'})
        expect("duplicate JSON key", "duplicate keys")
        install({"examples/demo.json": '{"data_classification":"synthetic","value":1e999}'})
        expect("decoded non-finite JSON number", "non-finite decoded JSON")
        install({"notes.txt": b"a" + bytes([0]) + b"b"})
        expect("binary content", "binary control")
        install({"notes.txt": bytes.fromhex("504b0304") + b"archive"})
        expect("disguised archive", "nested archives")
        install()
        (root / ".git").mkdir()
        (root / ".git" / "config").write_text("local metadata", encoding="utf-8")
        expect("clone metadata ignored", None)
        expect("package metadata rejected", "Git metadata", package_tree=True)
        install()
        cache = root / "tools" / "__pycache__"
        cache.mkdir()
        (cache / "demo.cpython-312.pyc").write_bytes(bytes([0]))
        expect("generated bytecode ignored", None)
        expect("package bytecode rejected", "bytecode caches", package_tree=True)
        (cache / "hidden.txt").write_text("Unexpected", encoding="utf-8")
        expect("cache cannot hide text", "bytecode caches")
        install()
        try:
            (root / "linked.txt").symlink_to(root / "README.md")
        except (OSError, NotImplementedError):
            print("NOTE: symlink self-test unavailable on this platform.")
        else:
            expect("symbolic link rejected", "symbolic links")
    print(f"PASS: {checks} offline validator self-tests.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="showcase directory (defaults to this checkout)")
    parser.add_argument("--package-tree", action="store_true", help="also forbid Git metadata and generated bytecode caches")
    parser.add_argument("--self-test", action="store_true", help="run small adversarial fixtures instead of checking this checkout")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    result = validate_tree(args.root.absolute(), package_tree=args.package_tree)
    if result.errors:
        print(f"FAIL: {len(result.errors)} public-showcase check(s) need attention.")
        for error in result.errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(result.files)} allowlisted public files checked offline.")
    print("Showcase checks only; no private trading-engine tests or exhaustive security guarantee.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

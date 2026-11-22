#!/usr/bin/env python3
"""Create a reproducible ZIP from validated, allowlisted public files only."""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import stat
import sys
import tempfile
import zipfile

# Importing the public checker must not create new source-tree files.
sys.dont_write_bytecode = True
from check_public import validate_tree  # noqa: E402


PACKAGE_ROOT = "Multisource_HL_Copy"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="showcase directory (defaults to this checkout)")
    parser.add_argument("--output", type=Path, help="ZIP destination outside the showcase; defaults to its parent directory")
    args = parser.parse_args()
    root = args.root.absolute()
    if root.is_symlink():
        print("FAIL: source root must not be a symbolic link.")
        return 1
    root = root.resolve()
    output = args.output.absolute() if args.output else root.parent / f"{PACKAGE_ROOT}-public.zip"
    if output.is_symlink():
        print("FAIL: output must not be a symbolic link.")
        return 1
    output = output.resolve()
    if output == root or root in output.parents:
        print("FAIL: write the ZIP outside the showcase directory.")
        return 1
    if output.suffix.lower() != ".zip" or not output.parent.is_dir():
        print("FAIL: output must be a .zip path in an existing directory.")
        return 1
    if output.exists() and not output.is_file():
        print("FAIL: output exists and is not a regular file.")
        return 1

    result = validate_tree(root)
    if result.errors:
        print("FAIL: packaging stopped because public-showcase checks failed.")
        for error in result.errors:
            print(f"- {error}")
        return 1

    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(prefix="public-package-", suffix=".tmp", dir=output.parent, delete=False) as handle:
            temporary = Path(handle.name)
        with zipfile.ZipFile(temporary, mode="w", compression=zipfile.ZIP_STORED) as archive:
            archive.comment = b""
            for name, content in sorted(result.files.items()):
                member = zipfile.ZipInfo(f"{PACKAGE_ROOT}/{name}", date_time=ZIP_TIMESTAMP)
                member.create_system = 3
                member.compress_type = zipfile.ZIP_STORED
                member.external_attr = (stat.S_IFREG | 0o644) << 16
                member.extra = b""
                member.comment = b""
                archive.writestr(member, content)
        # The ZIP contains the exact in-memory bytes that passed validation.
        with zipfile.ZipFile(temporary) as archive:
            expected = [f"{PACKAGE_ROOT}/{name}" for name in sorted(result.files)]
            if archive.namelist() != expected or archive.testzip() is not None:
                raise ValueError("archive integrity check failed")
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        os.replace(temporary, output)
        temporary = None
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"FAIL: could not create the public ZIP ({type(exc).__name__}).")
        return 1
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)

    print(f"PASS: packaged {len(result.files)} allowlisted files as {output.name}.")
    print(f"SHA-256: {digest}")
    print("Fixed timestamps, file modes, ordering, and uncompressed entries; no Git history or generated caches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

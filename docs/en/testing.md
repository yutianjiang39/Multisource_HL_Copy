# Evidence and verification limits

[中文](../testing.md) · [Home](../../README.en.md)

This page explains what a reader can independently inspect in the public repository. It is not a private-system test report and publishes no production test counts, deployment status, operating dates, or latency results.

## Three different kinds of material

| Kind | Examples here | What it can establish |
| --- | --- | --- |
| Capability descriptions | README, capabilities, responsibility overview | The project's concerns and product communication |
| Synthetic illustrations | SVGs, JSON, scenario guide | A way to read or present information |
| Executable local checks | File inventory, links, examples, and figure checks | Current public files meet the specific checked rules |

The first two do not prove real fills or production reliability. Passing the third does not validate the private engine, trading strategy, idempotency, recovery, or risk controls.

## Local validation

From the repository root, with Python 3.10 or newer:

```bash
python3 tools/check_public.py
python3 tools/package_public.py --output ../Multisource_HL_Copy-public.zip
```

The validator uses [public-files.txt](../../public-files.txt) as the release inventory. It checks paths, relative links, synthetic JSON labels, safe SVG structure, and selected sensitive patterns. The packager includes only listed files, excludes Git history, and checks the archive content again.

The tools do not query exchanges, read accounts, simulate trading, or inspect private code. They cannot detect every trade secret, semantic disclosure, visual meaning, or previously published history; human review remains necessary.

The CI workflow repeats only the public-content check. Its presence does not establish that remote CI has run.

## If measurement summaries are published later

Any summary should undergo a separate disclosure review and explain:

- The outcome measured and its definition.
- Sample selection, omitted samples, and applicability.
- Observed outcomes versus design goals.
- Uncovered conditions, negative results, and uncertainty.
- Whether evidence still applies to the version discussed.

Passing tests does not imply absence of defects. Limited samples should not become promises of universal fills, no duplicates, or returns. This edition does not publish production measurement data.

## Acceptance criteria for this edition

Chinese and English agree; images, text, and JSON identify synthetic material; unresolved results remain unresolved; relative resources open; interface outlines are excluded; the archive matches its inventory. These checks concern public-content quality and disclosure boundaries.

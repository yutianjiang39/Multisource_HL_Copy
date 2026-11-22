# Verification and evidence

[中文](../testing.md) · [Performance](performance.md) · [Home](../../README.en.md)

Capabilities, measurements, and necessary conditions should explain the project's strengths together. This page identifies the evidence behind each kind of claim.

## Four evidence classes

| Class | Included here | What it supports |
| --- | --- | --- |
| Mainnet measurements and run summaries | Local submission percentiles, end-to-end medians, three-target run summary | Performance and scale observed within the recorded samples and period |
| Simulated load acceptance | Two-source 150/s load, five-second bursts, ten runs | Request matching and tail latency under that simulated workload |
| Configuration and capability descriptions | Up to eight configured targets and responsibility descriptions | Support in the supplied configuration, not a saturation point |
| Synthetic experience and file checks | Scenario figures, examples/, local validation | Presentation, file structure, and disclosure rules |

Mainnet results, simulated results, and configuration ceilings are different kinds of evidence. Historical figures belong in [benchmarks/](../../benchmarks/README.md); fictional scenarios belong in [examples/](../../examples/README.md).

## Checks performed for this edition

- Matched values, sample counts, and units to retained project summaries.
- Distinguished local submission, simulator request receipt, exchange inclusion, and fills.
- Distinguished aggregate input rate, per-source rate, request matching, and actual fills.
- Checked configuration limits against recorded rehearsal and live scales.
- Retained unmeasured areas and conditions that limit extrapolation.
- Removed identities, deployment details, raw events, and mechanisms unnecessary to interpret the results.

This edition organizes existing records. It did not rerun the private engine, production load tests, or live trades. Historical build results do not automatically establish current-build performance.

## Minimum useful measurement metadata

Name, start/end boundary, unit, samples or runs, offered workload and window, live or simulated environment, version applicability, and limitations that materially change interpretation.

Sanitized hardware class, CPU class, and system load can help fair comparisons. Those fields are not fully retained in the current historical summaries and are left unspecified, not invented. Hosts, access details, and tuning settings need not be disclosed.

Current-build p95/p99, sustained throughput, eight-active-target load, error rates, and peak backlog can be added after measurement. Synthetic values are not substitutes.

## Local checks

Use Python 3.10 or newer:

```bash
python3 tools/check_public.py
python3 tools/check_public.py --self-test
python3 tools/package_public.py --output ../Multisource_HL_Copy-public.zip
```

The checker validates the inventory, relative links, JSON classifications and measurement metadata, SVG structure, and common sensitive patterns. It accepts curated measured_aggregate data instead of forcing real results to be labeled synthetic.

CI repeats file validation. It cannot reproduce private experiments, authenticate raw trades, or detect every misleading statistic. Passing a file check is distinct from passing a performance test.

## Updating results

Update both languages, [results.json](../../benchmarks/results.json), and the [performance figure](../../assets/performance.svg) together. Keep definitions stable; when boundaries or populations change, publish separate results rather than merge incompatible data. Retain raw evidence privately and publish sanitized statistics, definitions, and scope.

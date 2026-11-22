# Multisource HL Copy

**Multi-source copy-trading execution for Hyperliquid**

Event-driven · Rust execution · Multiple followed targets · Risk and operational visibility

[中文](README.md) · [Performance](docs/en/performance.md) · [Capabilities](docs/en/features.md) · [Overview](docs/en/architecture.md) · [Scenarios](docs/en/showcase.md) · [Public scope](docs/en/public-scope.md)

One execution account follows multiple sources, spanning order following, position changes, risk intervention, and reporting. The project focuses on low local processing overhead, burst-oriented signal handling, and multi-source operation.

![Performance summary: 43 ms local-submission p99, 150 signals/s burst tests, and eight configurable targets, each labeled with its evidence scope.](assets/performance.svg)

## Performance snapshot

| Strength | Recorded result | Scope |
| --- | --- | --- |
| **Low local submission latency** | **p99 43 ms · p50 24 ms** | 1,765 mainnet order samples, local receipt to recorded submission |
| **Burst signal handling** | **150 signals/s across two sources** | Three 5-second bursts per run, ten simulated runs; per-run p99 139–186 ms |
| **Target configuration** | **Up to 8 targets** | Total unique targets including the primary; not a full-load capacity claim |
| **Multi-source validation** | **3 live targets · 5 rehearsal targets** | About 80 minutes of mainnet operation and about 5 minutes of live-data rehearsal |
| **End-to-end mainnet observations** | **0.81 s placement · 0.67 s cancellation** | Medians in a small scripted-source test; 73 and 69 samples respectively |

These are sanitized summaries of the project's November 2026 historical records, not fictional display values. Results have different builds, workloads, and timing boundaries. The 43 ms figure excludes exchange confirmation; 150/s is a short-burst offered rate. See [Performance](docs/en/performance.md) and the [measurement data](benchmarks/results.json) for conditions, statistics, and unmeasured areas.

## Capabilities

| Capability | Operator value |
| --- | --- |
| **Multiple sources** | Organize several sources within one execution account with source context and outcome descriptions |
| **Order lifecycle** | Resting-order mirroring, changes, cancellations, and execution-state visibility |
| **Fills and position changes** | Taker opening, follow reductions, and remaining-position handling |
| **Operational control** | Start, stop, settings changes, and source adjustments |
| **Risk intervention** | Risk evaluation, pausing or stopping, cancellations, and position closing with visible outcomes and unresolved states |
| **Reporting and traceability** | Event notices, periodic reports, and operational records |

See [Capabilities](docs/en/features.md). A capability description does not guarantee fills, recovery, or loss limitation in every scenario.

## Engineering strengths

**Rust for real-time execution; Python for control and reporting.** Event-driven execution separates latency-sensitive processing from operator-facing responsibilities.

**Percentiles with workload definitions.** Local p99, simulated bursts, and mainnet end-to-end observations are reported separately, rather than combined into a nonexistent result.

**Layered multi-source evidence.** Configuration limits, live-data rehearsals, mainnet operation, and simulated load each have an explicit scope.

**An operational workflow.** The system addresses state observation, risk intervention, control, and reporting alongside request submission. Public descriptions retain responsibilities while algorithms and recovery mechanisms remain private.

## Two kinds of public material

| Material | Purpose |
| --- | --- |
| [benchmarks/](benchmarks/README.md) | Sanitized historical results, classified as measured_aggregate |
| [examples/](examples/README.md) | Fictional presentation examples, classified as synthetic |

> This is a public showcase. The production trading implementation remains private. There is no account connection, signing, or trading runtime here. Synthetic scenarios and measured performance are labeled separately.

## Reading guide

| Question | Page |
| --- | --- |
| Recorded latency, load, and target scale | [Performance](docs/en/performance.md) |
| Product capabilities | [Capabilities](docs/en/features.md) |
| Technical responsibilities and boundaries | [Overview](docs/en/architecture.md) |
| Following, risk, and reporting experience | [Scenarios](docs/en/showcase.md) |
| Evidence and verification levels | [Verification](docs/en/testing.md) |
| Other questions | [FAQ](docs/en/faq.md), [Roadmap](docs/en/roadmap.md), [Releases](RELEASES.md) |

## Local viewing and maintenance

Read the documents, SVGs, and JSON directly. With Python 3.10 or newer, validate and package this public repository:

```bash
python3 tools/check_public.py
python3 tools/package_public.py --output ../Multisource_HL_Copy-public.zip
```

These tools process public files only and do not connect trading accounts. See [Maintenance](docs/maintaining-public.md). Suggestions on wording, measurement definitions, and presentation are welcome through [Contributing](CONTRIBUTING.md).

## Disclosure and rights

Performance results, necessary test conditions, and engineering capabilities can be public. Execution algorithms, strategy settings, real identities, raw trades, and deployment access remain private; see [Public scope](docs/en/public-scope.md).

See [LICENSE](LICENSE); previous permissions still apply to corresponding material. No returns are promised. Hyperliquid identifies the platform concerned and does not imply affiliation or endorsement.

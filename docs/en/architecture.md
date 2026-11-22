# System overview

[中文](../overview.md) · [Performance](performance.md) · [Home](../../README.en.md)

Multisource HL Copy uses an event-driven Rust core for real-time execution and Python for control, configuration, and reporting. Public architecture describes responsibilities and trade-offs without exposing internal interfaces, execution algorithms, or recovery state machines.

## High-level responsibilities

| Area | Responsibility | Engineering value |
| --- | --- | --- |
| Control and configuration | Operator entry points, effective settings, start/stop, and source changes | Make scope and changes understandable |
| Real-time execution | Source events, order lifecycle, and position-related actions | Focus on local overhead and execution consistency |
| Risk and state | Risk evaluation, state records, intervention outcomes, and unresolved facts | Keep operational uncertainty visible |
| Reporting and traceability | Event notices, periodic summaries, and operational records | Support review and investigation |

The Rust/Python division is public technical context. Modules, internal protocols, queues, persistence sequencing, and scheduling rules remain private.

## Evidence for design goals

| Concern | Public evidence | Reading guide |
| --- | --- | --- |
| Local overhead | 43 ms local-submission p99 across 1,765 mainnet order samples | Local latency in the performance page |
| Burst handling | Aggregate 150/s across two sources, three five-second bursts, repeated simulated acceptance | Workload conditions |
| Multiple sources | Eight configurable targets, five-target rehearsal, three-target live summary | Scale and evidence levels |
| An operational workflow | Orders, positions, risk intervention, control, and reporting | Capabilities and scenarios |

Measurements describe historical conditions and do not turn one local metric into an end-to-end guarantee. Units, samples, and boundaries are in [Performance](performance.md).

## The operator's view

![Sources, execution concerns, and operational visibility. A synthetic concept illustration.](../../assets/overview.svg)

The source view describes intent changes; the execution view describes observed outcomes; risk and reporting views identify facts needing attention. The figure illustrates information relationships, not production modules or scheduling order.

Source intent and follower fills, local state and whole-account risk, request submission and final outcomes should remain distinct. This makes capabilities understandable without hiding uncertainty.

Continue with [Capabilities](features.md), [Performance](performance.md), and [Scenarios](showcase.md).

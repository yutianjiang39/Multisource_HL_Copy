# Overview: responsibilities from an operator's perspective

[中文](../overview.md) · [Home](../../README.en.md)

![Sources, execution concerns, and operational visibility. A concept illustration.](../../assets/overview.svg)

This page describes product responsibilities. Its groups do not correspond to production modules, deployment units, threads, databases, or communication links, and imply no internal execution order.

## Four areas of attention

| Area | Operator question | Information that may be presented |
| --- | --- | --- |
| Sources | Which sources are observed, and what changed? | Anonymous labels, summarized activity, and observation status |
| Execution | What happened on this side, and what is unknown? | Qualitative order and position states, outcome notes, and unresolved items |
| Operations and risk | What is in scope, and what needs attention? | Scope notes, operation records, risk descriptions, and review items |
| Reporting | What changed, and what comes next? | Source summaries, state changes, open questions, and evidence notes |

The project uses Rust and Python. This showcase retains only that high-level information, without a module inventory, interface outline, call graph, or runtime path.

## Distinctions that matter

**Source intent and execution outcome.** A source creating, changing, or ending an order is an observation. Whether the execution side places or fills an order, and whether risk remains, are separate facts.

**State descriptions and safety guarantees.** Labels such as “needs attention” and “awaiting confirmation” communicate information. They do not establish that a risk has been resolved. Completion needs appropriate evidence; this package supplies no production evidence.

**The scope of a view and the whole account.** A card may cover only one scenario or object. Local results should not be presented as proof that all account risk is cleared.

**Reports and decisions.** A report can organize known facts and open questions. A polished presentation does not establish profitability or make trading decisions for an operator.

## Product trade-offs

| Concern | What should be clear | Disclosure boundary |
| --- | --- | --- |
| Multiple sources | Separate source observations from execution results | No allocation, conflict-resolution, or sizing rules |
| Uncertainty | Make unresolved facts visible | No recovery, retry, or scheduling recipes |
| Explainability | Provide context and useful review items | No real logs, internal fields, or individual trade evidence |
| Operations | Explain intent, scope, and observable results | No production commands, permissions, or deployment steps |
| Credible verification | Separate descriptions, illustrations, and evidence | Repository checks do not validate the trading engine |

Continue with [Capabilities](features.md), [Scenarios](showcase.md), and [Evidence & limits](testing.md).

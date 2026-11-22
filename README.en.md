# Multisource HL Copy

**Multi-source trading execution engine for Hyperliquid**

Event-driven · Rust execution core · Fault-tolerant · Risk-aware

[中文](README.md) · [Architecture](docs/en/architecture.md) · [Features](docs/en/features.md) · [Showcase](docs/en/showcase.md) · [Testing & methodology](docs/en/testing.md) · [Releases](RELEASES.md)

---

One execution account follows the perpetual-futures orders of several Hyperliquid source wallets at once: it mirrors resting orders proportionally, follows reduces and taker opens, and pauses, cancels or flattens on risk events. Copy trading is the application; the focus of the project is the execution system behind it — how events from multiple sources are attributed, how each order's lifecycle is closed out, and how the system avoids duplicates, refuses to guess and stops safely when something is wrong.

> This is a **showcase repository**. It explains what the system does, how it is layered and how far it has been verified. The production implementation is private; there is no runnable trading program and no demo here. See [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md) (Chinese).

![A normal follow: source action → system response → final state (illustrative data)](assets/follow_flow.svg)

## The problem

Naive copy trading breaks under multiple sources, rapid place/cancel cycles, disconnects and partial fills: an order is placed twice, the source cancels but the mirror stays, two sources cancel each other out on the same coin, or the bot trades on stale data after a reconnect. This project treats those cases as first-class concerns. The goal: **keep up, cancel cleanly, reconcile exactly, and stop first when in doubt.**

## Layers

| Layer | Responsibility | Implementation |
|---|---|---|
| **Control plane** | Config validation, start plans, lifecycle (start / stop / retune / switch source), multi-version deployment; sensitive actions need explicit human authorization | Python |
| **Execution core** | Consumes source and own-account events; admission, risk accounting, place, amend, cancel, follow reduces, residual cleanup and recovery. Python is not on the hot path | Rust |
| **State & risk** | Durable state guarantees each source order is handled once; in-process drawdown stop plus an independent external guard | Rust and Python |
| **Observability** | Real-time event notifications, periodic reports, rolling incident trace | Rust and Python |

## Design goals

1. **Idempotent execution** — each source order is claimed once, even across crashes; orders with an unknown outcome are never resent blindly.
2. **Stop on insufficient evidence** — incomplete data, failed reconciliation or uncertain scope pauses trading instead of guessing.
3. **Source isolation** — a coin belongs to one source at a time, first come first served; blocked signals are recorded separately.
4. **Layered risk** — in-process stop and an external guard; different events pause new orders, cancel while keeping positions, or flatten.
5. **Humans decide** — start, stop, flatten, deploy and config changes all require authorization; the program itself only performs risk stops.

## Capabilities and maturity

Status levels: **implemented** (automated tests) → **deployed** (on the server) → **live-verified** (run against real sources on mainnet and checked).

| Capability | Status |
|---|---|
| Full order following: mirroring, in-place amend, cancel, taker open, follow reduce, residual cleanup | Live-verified; later edge-case fixes deployed, pending live re-check |
| Multi-source: per-coin ownership, first come first served, blocked signals reported | Live-verified; a per-source ratio fix is not yet deployed |
| Risk control: in-process drawdown stop + external guard, three actions | Deployed, always on in live runs |
| Runtime changes: instant / rebuild retuning, source switch, automatic rollback | Instant retune used live; source switch verified in tests only |
| Recovery: dual data feeds, pause and grace on disconnect, reconcile on resume | Deployed, in use during live runs |
| Reports & alerts, dry-run rehearsal, rolling incident trace | Deployed |

## Measured results (aggregate only)

| Category | Result | Conditions |
|---|---|---|
| Automated tests | 471 Python, 326 Rust, all passing | 2026-11-21, full suite on the server |
| Shadow test: scenarios | 9 scenario types, two rounds; every conclusive case behaved as designed, no leftover orders, local state matched the exchange | 2026-11-16, mainnet, small account, single source, ~5 min per round |
| Shadow test: end-to-end latency (median) | ~0.8 s to place, ~0.7 s to cancel; ~0.2 s of that is this system, the rest is exchange confirmation | Same; exchange timestamps |
| Multi-source live run | Three sources for ~80 minutes, ended flat | 2026-11-19, mainnet, small account |

These numbers describe execution correctness and latency. They are **not evidence of profitability** and do not generalize to all wallets or market conditions.

## License

Text and images: CC BY 4.0. `outline/` illustrative code: MIT. See [LICENSE](LICENSE). The private production implementation is not covered. Nothing here is investment advice.

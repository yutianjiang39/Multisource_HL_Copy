# Architecture

![System overview (illustrative)](../../assets/overview.svg)

The system has four parts. Arrows show the rough direction of information only, not real protocols or scheduling order.

| Part | Responsibility | Implementation |
|---|---|---|
| **Control** | Local entry point: builds a start plan, then — after human confirmation — starts, stops, retunes, switches sources and deploys. Sensitive actions without explicit authorization are refused | Python; authorization and command details are private |
| **Execution** | Consumes source and own-account events; admission, risk accounting, placing, amending, cancelling, following reduces, residual cleanup and recovery. The hot path never goes through Python | Rust execution engine, **private** |
| **State & reporting** | The state store guarantees each source order is handled once; a guard process checks risk independently; real-time events and periodic reports | Python and Rust |
| **Incident trace** | Records every input to the execution core, keeping a rolling window for after-the-fact investigation | Rust, written in the background |

## Boundaries

- **Python is not on the hot path.** The control plane handles config, start, stop and retuning; everything from receiving a source event to sending an order happens inside the Rust core.
- **The core only reacts to events.** Source pushes, own-account pushes and exchange responses enter the core as events and drive order state; control-plane changes enter as commands rather than editing core state directly.
- **Two independent risk layers.** The in-process stop uses a live equity estimate and reacts fast; the external guard reads directly from the exchange with the same rules and does not depend on the trading process being healthy.
- **Nothing counts until it is persisted.** Key steps such as claiming a source order and sending an order are written to disk first; restarts recover from that record instead of guessing from memory.

## Trade-offs

| Trade-off | Choice | Cost |
|---|---|---|
| Correctness vs follow rate | Pause or skip when evidence is insufficient | Some signals are missed during disconnects or inconsistencies |
| Multi-source conflicts | One source per coin; no stacking or netting | Later sources are blocked on that coin |
| Orders with unknown outcome | Never resent automatically; wait for a confirmed final state, escalate to a human if needed | Occasional manual intervention |
| Runtime changes | Apply instantly where possible; otherwise cancel (keep positions) and rebuild; roll back if the new config fails | Rebuild-level changes pause for seconds to tens of seconds |
| Deployment | Multiple code versions side by side; each instance pinned to its start version | Explicit version switches, more disk on the server |

## Deployment shape

- Each server runs one or more independent instances, each with its own account, sources, state store and keys.
- There is no web panel: operators use a local command-line assistant and receive notifications through instant messaging.
- Mainnet only. In dry-run the own side uses a local ledger while sources are still read from mainnet.
- A running instance stays on the code version it started with, so deploying a new version does not interrupt live trading.

Outline code is in [outline/](../../outline/). It only illustrates responsibilities and is not the production implementation.

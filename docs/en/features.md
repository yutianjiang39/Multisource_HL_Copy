# Features

Each item covers the scenario, the effect and the limits. Status terms:

- **Implemented** — code complete with automated tests.
- **Deployed** — code is on the server and can be enabled at any time.
- **Live-verified** — run against real sources on mainnet and checked item by item.

As of 2026-11-21 the private repository's full suite on the server passed: 471 Python and 326 Rust tests. Test counts show the amount of verification work, not the absence of defects. See [Testing & methodology](testing.md).

## 1. Multi-source following

**Scenario:** follow several wallets with different styles from one account without them fighting over the same coin.

**Effect:**
- Each source has its own follow ratio; all sources share the account-level risk limits.
- A coin belongs to one source at a time: the first source to signal takes it; ownership is released once the own account has no position, no resting order and no pending follow action on that coin.
- Blocked signals are counted separately and reported apart from "missed" and "blocked by risk".

**Limits:** no stacking or netting of several sources on one coin; proportional following only.

**Status:** per-coin ownership and blocking were live-verified on 2026-11-19 with three sources for about 80 minutes on a small account. An event-ordering issue found during that run was fixed; the fix is deployed but not yet re-verified live.

**Correction (2026-11-22):** per-source ratios used to be cleared — falling back to the global ratio — whenever the server started an instance or applied a runtime retune. The 2026-11-19 run therefore followed every source at the same ratio, and per-source ratios were **not** live-verified. The fix has a regression test and is not yet deployed.

## 2. Full order following

**Scenario:** reflect the source's placing, amending, cancelling, fills and reduces on the own account quickly and proportionally.

**Effect:**

| Source action | Own action |
|---|---|
| New resting order | Proportional maker-only mirror, price offset outward per config |
| Price change only | Amend in place, no cancel-and-replace |
| Cancel | Cancel the mirror |
| Taker open | IOC follow at the source fill price within a slippage cap |
| Reduce / close | Reduce-only by the source's reduce fraction; close entirely when the source goes flat |
| Source no longer holds, own side still does | Periodic scan plus event triggers close the residual reduce-only |

- Each source order is claimed exactly once; a crash and restart never places it twice.
- An order that was sent but whose outcome is unknown is never resent automatically; the system waits for a confirmed final state.

**Limits:** perpetual regular orders only — no spot, no trigger orders. Orders that fall below the exchange minimum after scaling are skipped or topped up per config.

**Status:** live-verified (see [Showcase](showcase.md), scenario 1). Later fixes for races and partial-fill edge cases are deployed but not yet re-checked live.

## 3. Risk control

**Scenario:** stop in time when the source takes a large loss, the own side diverges from the source, or orders appear that this program did not place.

**Effect:**
- The trading process estimates equity in memory; if drawdown from the run's peak exceeds the limit for a short while, it stops and flattens. Deposits and withdrawals do not affect the figure.
- An independent guard process checks the exchange periodically with the same rules as a backstop, and also checks aggregate positions, direction and deviation, and foreign orders.
- Events map to three actions: **pause new orders**, **cancel but keep positions**, **flatten**. Every action sends a notification.

**Limits:** thresholds and calculation details are private. Stops execute at market and may fill worse than the trigger; risk control promises neither profit nor a maximum loss.

**Status:** both layers are deployed and always on in live runs; trigger paths are covered by automated tests.

## 4. Runtime changes

**Scenario:** change ratios, limits or switches while following, or swap a source.

**Effect:** every change is previewed first and classified:
- **Instant** — ratios, limits, follow switches, etc.; effective from the next order with no pause.
- **Rebuild** — coin scope, concurrency profile, etc.; cancels this program's orders, keeps positions and resumes with the new parameters after seconds to tens of seconds.
- **Source switch** — requires the own side to be flat with no orders; old state is archived and the stop's equity and peak carry over.

Outcomes are one of four: applied, rejected, failed, rolled back — all audited. If the new config cannot start, the original is restored automatically.

**Limits:** account, network and run mode cannot change at runtime.

**Status:** instant retuning was used once live on 2026-11-19 (changing the stop limit) and behaved as expected. More fields have since become instant-level; that is deployed but not yet live-verified. Source switching is verified in tests only.

## 5. Recovery

**Scenario:** feed disconnects, request timeouts, process faults.

**Effect:**
- Two independent data feeds. If one drops while the other keeps pushing, reduces and cleanup continue. If both drop, new orders pause and resting mirrors follow a grace period.
- After reconnecting the system re-reads and reconciles; coins that do not match are flagged and held until verified.
- Orders with unknown outcomes are not assumed to have succeeded or failed; a human resolves them from the record if needed.
- Shutdown order: stop new orders → cancel → reconcile → persist.

**Limits:** not every fault recovers automatically. A crashed process is not restarted automatically; it alerts and a human decides.

**Status:** deployed and in use during live runs.

## 6. Reports and alerts

**Scenario:** no panel and nobody watching constantly — the system must tell people what happened.

**Effect:**
- Real-time events: opens, adds/reduces, closes (with holding time and realized PnL), flips, margin usage, drawdown warnings, follow anomalies. Batched and rate-limited.
- Periodic reports: replication quality, deviation from sources, fill prices and latency, period and cumulative PnL, missed and risk-blocked signals, and an "attention" section.
- An AI assistant on the server reads only logs and metrics and adds an anomaly analysis to the report.

**Limits:** no web panel. The report image in the showcase is a re-laid-out illustration with synthetic data.

**Status:** deployed, in live use.

## 7. Dry-run rehearsal

**Scenario:** try a new source or new parameters without placing real orders.

**Effect:** sources are still read from real mainnet activity; the own side uses a local ledger to simulate fills and balances; following, risk and reports run as usual.

**Limits:** rehearsal results prove nothing about real fills, margin or profit.

**Status:** deployed, used many times.

## 8. Rolling incident trace

**Scenario:** after a problem, find out what the system received and what it decided.

**Effect:** every input to the execution core and every exchange call is recorded in compressed segments, written in the background without slowing trading. Each instance keeps a rolling window with a size cap; if the queue is full one segment is dropped and marked, and recording continues.

**Limits:** recent history only. Offline replay has been removed from the main program; it records but does not replay.

**Status:** deployed; no trace has yet been produced during a live run.

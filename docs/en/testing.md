# Testing & methodology

How the project is verified and how public numbers are reported. Aggregates only — no individual orders, raw logs or event timelines.

## Verification layers

| Layer | What it does | What it proves | What it does not prove |
|---|---|---|---|
| **Unit tests** | Config validation, risk decisions, report calculations, control commands | Modules behave as specified | How modules work together |
| **Core scenario tests** | Drive the Rust execution core with constructed source and own-account events; check orders, state and risk accounting | Races, partial fills, disconnects and restarts behave as designed, repeatably | Real exchange acceptance and fills |
| **Mock exchange** | Run the execution program end to end against a test exchange | Process-level start, stop, recovery and persistence | Real network latency and exchange rules |
| **Dry-run** | Real mainnet sources, local ledger for the own side | Follow decisions, risk and reports under real source rhythm | Real fills, margin and profit |
| **Shadow test** | Scripted test wallet as source, follower live on mainnet with a small account | Main paths work on the real exchange; latency is measurable | Real source behaviour, long runs |
| **Live runs** | Real sources, small mainnet account | Behaviour under real conditions over time | Large capital, extreme markets |

The three status levels (implemented / deployed / live-verified) follow this table: anything verified only by the first four layers is at most "deployed".

## Automated test scale

| Date | Python | Rust | Result |
|---|---|---|---|
| 2026-11-21 | 471 | 326 | All passing |

Run in full on the server. Scenario categories include core following, follow reduces, taker opens, multi-source ownership, disconnects and grace periods, fault injection, control handoff, emergency stop and flatten, runtime retuning, ledger and fund flows, new listings, and request budgets. Test counts show verification effort, not the absence of defects.

## Reporting rules

- **Aggregates only.** No breakdown by source, coin or account; no individual orders or timelines.
- **Conditions stated.** Every number carries its date, environment (mock / shadow / live), sample range and tested version; numbers from different conditions are not compared directly.
- **Scale as magnitude only.** Account size and order size are described as "small" or "close to the exchange minimum", never exact.
- **Latency on exchange timestamps.** End-to-end latency runs from the source order becoming effective to the mirror becoming effective, both on exchange timestamps, unaffected by server clock skew; segment timings state their clock source.
- **Not profitability.** Execution latency and reliability say the system keeps up and reconciles, not that copying makes money.
- **Results age.** Fixes after a test do not make old results hold for the new version; anything not re-run is marked as such.

# Features

[中文](../features.md) · [Project home](../../README.en.md) · [Scenario guide](showcase.md) · [FAQ](faq.md)

This page describes product capabilities, use cases, and observable outcomes. **These are capability descriptions, not implementation, deployment, or live-operation claims verified by this repository.** The repository contains documentation, conceptual illustrations, and synthetic data. It does not include a trading system that connects to accounts, receives live market data, or submits orders.

Illustrations and examples are marked **SIMULATED / 合成示例**. Their sources, assets, states, and values are entirely fictional; the illustrative screens are not production screenshots. See [PUBLIC_SCOPE.md](../../PUBLIC_SCOPE.md) for publication boundaries and [Verification scope](testing.md) for how to read the evidence.

## Capability overview

| Capability | Question it aims to help a user answer | Public reading material |
|---|---|---|
| Multiple-source organization | Which sources are in view, and where did a record originate? | This page and the multiple-source scenario |
| Order and position lifecycle | How does a source action relate to later states? Which outcomes remain unclear? | Following illustration and synthetic scenario |
| Risk information and intervention outcomes | What was flagged, what action was recorded, and what still needs attention? | Risk illustration and synthetic event |
| Configuration and scope changes | What should change, and which states deserve attention afterwards? | The change discussion on this page |
| Uncertainty and human review | What is known, and what cannot yet be concluded? | Scenario guide and sample report |
| Reports and notifications | What happened during a period of activity, and where should a reader look next? | Report illustration and synthetic report |
| Rehearsal and scenario discussion | How can expected behavior be discussed before real trading? | Static synthetic examples |
| Traceable explanations | How can a reader move from a summary to its relevant context? | Source labels, scenario descriptions, and event notes |

These materials demonstrate how information can be presented. They are not an operational console or a running feature demonstration.

## 1. Multiple-source organization

**Use case:** a user wants to understand several sources in one view without repeatedly reconstructing context from scattered records.

**Capability description:** keep source identity, related assets, and activity states recognizable, so a summary still indicates which source a record concerns. A multiple-source view should also help a reader spot differences that need explanation.

**Publicly visible:** SOURCE_A, SOURCE_B, ASSET_X, and ASSET_Y represent entirely fictional sources and assets. Readers can assess whether labels are clear and whether summaries connect to the relevant scenarios.

**Boundary:** displaying several source records together does not mean that they would produce simultaneous trades, and it does not explain capital allocation, execution priority, or source-conflict handling. The synthetic identifiers are not wallet addresses or tradable-asset configuration.

## 2. Order and position lifecycle

**Use case:** after a source creates an order, changes its trading intent, or changes its position, a user wants to understand the status of related records.

**Capability description:** describe source actions and related responses around common activities such as placing, modifying, and cancelling orders, increasing or reducing positions, and closing positions. Order lifecycles, position changes, and observable outcomes should remain distinct. An action at the source does not mean that the following account necessarily obtains the same result.

| Reading subject | Information to convey |
|---|---|
| An order appears | A source has a new trading intent, with a related response description |
| Intent changes | A related record changes, with its earlier context still understandable |
| An order ends | How the current record describes the end of that order |
| A position changes | What changed in the position summary and whether a difference needs attention |
| An outcome remains unclear | Available information does not confirm the result, so it must not be presented as complete |

**Publicly visible:** the [following scenario](showcase.md#journey-one-understand-an-order-lifecycle) and [synthetic scenario data](../../examples/scenario.json) illustrate this organization of information.

**Boundary:** public materials do not expose order construction, sizing calculations, execution paths, or confirmation mechanisms. They do not establish that real orders will fill, reproduce source activity fully, or achieve the same profit or loss.

## 3. Risk information and intervention outcomes

**Use case:** when account activity raises a concern, a user needs to understand the warning, the described intervention, and what remains unresolved.

**Capability description:** relate risk information to the relevant source, asset, or account context. Outcomes such as pausing new activity, cancelling orders, or addressing positions need understandable descriptions. Unconfirmed results should remain explicit.

**Publicly visible:** the [risk-event illustration](showcase.md#journey-three-read-a-risk-notice-and-its-outcome) and [synthetic event data](../../examples/risk-event.json) show how to distinguish an event description, a recorded action, and an open question.

**Boundary:** examples do not establish a fixed mapping between real events and actions, and do not disclose thresholds, calculations, or control ordering. Describing a risk capability does not guarantee a loss limit, an execution result, or account safety.

## 4. Configuration and scope changes

**Use case:** a user wants to change the sources, asset scope, or other product settings under consideration and understand which activities might be affected.

**Capability description:** distinguish the requested change, the settings currently presented, and any result record associated with that change. This supports review of what changed, what it concerns, and what still needs confirmation.

**Publicly visible:** this page describes the information that matters to a change-review experience. The repository contains no real parameter table or executable configuration example.

**Boundary:** there is no administration interface here, and changes cannot be applied. Public illustrations do not establish which fields can change, when changes take effect, what operating conditions they require, or how failures are handled.

## 5. Uncertainty and human review

**Use case:** when state is missing, records differ, or a report does not fully explain an activity, a user needs to know which conclusions remain unsupported.

**Capability description:** separate known information from open questions and retain useful context for human review. An exception summary should point to facts that need examination without presenting a hypothesis as an established cause.

**Publicly visible:** differences, attention items, and outcome descriptions in the scenarios and report let readers assess whether the wording is sufficiently clear.

**Boundary:** these materials contain no fault-recovery procedure, retry rules, or operational response guide. They do not imply that all exceptions can be resolved automatically.

## 6. Reports and notifications

**Use case:** a user cannot monitor all activity continuously and needs a readable summary that identifies what deserves attention.

**Capability description:** organize reports around source activity, outstanding orders, position summaries, relevant differences, and attention items. An event notification focuses on one change worth reviewing; a periodic summary supports an overall view. A reader should be able to distinguish the overall activity summary from an unconfirmed outcome in a particular record.

**Publicly visible:** the [report illustration](showcase.md#journey-four-read-an-activity-report) and [synthetic report data](../../examples/report.json). Explanatory text demonstrates a style of presentation, not a diagnosis of a real account.

**Boundary:** this repository sends no notifications and provides no live reporting service. Synthetic totals are not trading records, profit statistics, latency measurements, or reliability evidence.

## 7. Rehearsal and scenario discussion

**Use case:** when discussing a new source or product settings, participants first clarify the states and report content they would expect to see.

**Capability description:** rehearsal can support discussion of expected behavior, reveal missing scenarios, and help assess whether state descriptions are understandable.

**Publicly visible:** the repository provides static synthetic examples for step-by-step reading or review discussions. They are not an executable trading simulator.

**Boundary:** reading a fictional scenario is not a backtest, a simulation run, or real-market validation. The examples do not model liquidity, fill probability, fees, margin, or returns.

## 8. Traceable explanations

**Use case:** a reader notices an exception or difference in a summary and wants to find its relevant source and scenario.

**Capability description:** use clear labels and related descriptions to connect the overall summary to specific context, supporting discussion of what happened and what is currently known.

**Publicly visible:** the relationship between documentation, illustrations, and synthetic data. Readers can directly assess the clarity of those public materials.

**Boundary:** the repository provides no production logs, individual fills, account history, or internal recording formats. Public scenarios cannot replace an investigation of real activity.

## What visitors can evaluate

| Can be evaluated from this repository | Cannot be evaluated from this repository alone |
|---|---|
| Clarity and consistency of product descriptions | Whether private features are implemented, deployed, or live-verified |
| Whether sources, events, and outcomes are easy to distinguish | Correctness of multiple-source execution or sizing |
| Whether examples disclose their synthetic nature and limits | Real execution speed, following quality, or long-term availability |
| Readability of risk notices and attention items | Whether risk controls limit real losses |
| Alignment of Chinese, English, illustrations, and data | Profitability under any market conditions |

## Frequently asked questions

**Can I connect an account or start trading?**  
No. This is a showcase package without a trading runtime, account integration, or executable production configuration.

**Are the illustrations actual product screens?**  
No. They were created to explain information relationships and do not establish the existence of an administration panel or live service.

**What is the product context and public support scope?**  
The product context is multiple-source following for perpetual contracts. Public materials discuss orders, positions, risk, and reports. They do not imply a compatibility commitment for any particular market, order type, or third-party service.

**Why might a source action lack a corresponding trading result?**  
A public example may show only part of a situation. “A source action occurred,” “a response was recorded,” and “an outcome was confirmed” are distinct statements. A static illustration cannot establish the private system's decision rationale.

**How can I provide useful feedback?**  
Identify the document location, unclear wording, or missing reading scenario, and use fictional identifiers to explain the issue. Real account details and operational records are not needed for public feedback.

**How may these materials be used?**  
See [LICENSE](../../LICENSE) and [Public scope](../../PUBLIC_SCOPE.md) for applicable terms. Capability descriptions do not grant access to the private implementation.

Continue with the [Scenario guide](showcase.md) or the [Public showcase roadmap](roadmap.md).

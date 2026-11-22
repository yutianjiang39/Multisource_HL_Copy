# Public scope and disclosure boundaries

[中文](../../PUBLIC_SCOPE.md) · [Home](../../README.en.md)

This edition introduces the project's capability themes, user experience, and engineering concerns. It contains rewritten explanations and independently constructed synthetic scenarios, not a production trading program.

## Included materials

| Material | What it explains | What it does not establish |
| --- | --- | --- |
| Bilingual introduction and capabilities | Concepts, terminology, and operator questions | Verification of the current production release |
| Responsibility overview | Product boundaries around control, execution, risk visibility, and reporting | Internal modules, call order, or real deployment topology |
| SVG illustrations | How information can be presented | Actual UI, account state, or trading outcomes |
| Synthetic JSON examples | Fields used by these presentation materials | A production API, configuration, or event contract |
| Validation and packaging utilities | Public file structure, selected sensitive patterns, and publication scope | Private-engine test results or exhaustive detection |
| Public release notes | Presentation-material changes | Private commits, deployments, fixes, or operating timelines |

## Kept private

Execution algorithms, allocation and conflict rules, recovery and risk decisions, internal interfaces, state machines, scheduling details, parameters, complete configuration, deployment and access details, source research, identities, addresses, capital, individual trades, production logs, databases, original screenshots, private test vectors, and internal review findings are outside this edition.

Private test counts, live-run dates, latency breakdowns, and fix lists are also omitted. This is a disclosure choice, not a finding that earlier reported results were false.

## Synthetic examples

Every example is marked **SIMULATED / 合成示例** and uses fictional identifiers such as SOURCE_A and ASSET_X. Each JSON example declares `data_classification: synthetic`.

Examples are authored from scratch, not renamed exports of real logs. They contain no real-format addresses, capital, return, latency, or actual timestamps. Their fields are for this showcase only.

An example may leave a result unresolved. Source intent, request submission, and actual fills are not treated as necessarily identical. Risk categories are not mapped to fixed production actions.

## Combined disclosure

Names, rules, diagrams, interfaces, and operating metrics can reveal more together than separately. Review prose, figures, examples, comments, paths, and history together.

This edition removes interface outline code in favor of concept descriptions. The only programs are generic local validation and packaging utilities.

## History and rights

This ZIP contains no Git history, raw operating data, or production implementation. It cannot erase earlier public history, forks, caches, or downloads. When updating an existing repository, also remove files listed in [REMOVED_FILES.txt](../../REMOVED_FILES.txt); overwriting matching names is insufficient.

[LICENSE](../../LICENSE) reserves rights in new original material while preserving earlier grants. The exact legacy notice is in [LICENSES/LEGACY_LICENSE.txt](../../LICENSES/LEGACY_LICENSE.txt). Previously licensed portions, including reused portions, remain subject to their applicable earlier license. This notice does not remove platform permissions to view or fork, or uses allowed by law.

Public material can still be read and learned from. Protection here comes from limiting implementation disclosure; the documents, license, and checks do not make copying impossible.

See [Contributing](../../CONTRIBUTING.md) and [Security](../../SECURITY.md) for feedback. This showcase promises no returns, fill rate, recovery time, or loss-stop outcome.

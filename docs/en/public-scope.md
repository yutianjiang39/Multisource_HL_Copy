# Public scope and disclosure boundaries

[中文](../../PUBLIC_SCOPE.md) · [Home](../../README.en.md)

This edition presents Multisource HL Copy's coordination across sources and engineering results, including documented historical aggregates for latency, burst signal handling, concurrent sources, and test coverage. Public results can be specific and checkable while trading implementations, account data, and production configuration remain private.

## Included materials

| Material | What it explains | What it does not establish |
| --- | --- | --- |
| Bilingual introduction and capabilities | Product capabilities, engineering priorities, and operator questions | Verification of every description in the current production release |
| [Performance and validation](performance.md), [measurement aggregates](../../benchmarks/results.json) | Documented historical results, measurement scope, and known limitations | Latest-release results, untested capacity limits, or future operating guarantees |
| Responsibility overview | Product boundaries around control, execution, risk visibility, and reporting | Internal modules, call order, or real deployment topology |
| Performance charts | Visualizations of published measurement aggregates | Performance conclusions beyond the associated measurement scope |
| Concept illustrations and synthetic scenarios | How information can be presented | Actual UI, account state, or trading outcomes |
| Synthetic JSON examples under `examples/` | Fields used by these presentation materials | A production API, configuration, or event contract |
| Validation and packaging utilities | Public file structure, selected sensitive patterns, and publication scope | Private-engine test results or exhaustive detection |
| Public release notes | Presentation-material changes | Private commits, deployments, fixes, or operating timelines |

## Measurement results that can be published

Documented, sanitized measurement summaries use `data_classification: measured_aggregate` and are stored separately from synthetic examples. Publishable results include:

- Directly measured latency percentiles, including p99; burst signal throughput at a named processing layer; and tested concurrent-source counts.
- Test categories, aggregate test counts, tested-target counts, statistical sample sizes, duration, and error or drop rates with their denominators explained.
- Generic measurement start and end boundaries, anonymized environment classes, and historical periods or version attribution at a publishable level of detail.

This metadata provides the context needed to interpret a benchmark; it is not automatically a secret implementation detail. Publish only values supported by records. Mark missing conditions as unrecorded instead of filling them with estimates. See [Performance and validation](performance.md) and the [benchmark data guide](../../benchmarks/README.md).

Preserve the scope of each result: a tested source count is not a capacity ceiling; p99 cannot be inferred from p50; signal-processing throughput is not exchange order or fill throughput; and a short burst does not establish sustained-load performance. Label historical measurements as historical rather than presenting them as a fresh validation of the latest release.

## Kept private

The following remain private:

- Execution algorithms, quantitative allocation, conflict handling, recovery, and risk decisions.
- Internal interfaces, state machines, dependencies, event priorities, timing, and retry conditions.
- Operating parameters, thresholds, defaults, complete configuration, and paths, hosts, or access details that identify a deployment.
- Source research, real identities, account identifiers, addresses, capital, and individual trades.
- Production logs, databases, original screenshots, private test vectors, and internal review findings.

Publishing test counts, result-level latency, and environment classes does not require publishing test vectors, execution mechanisms, production operating schedules, or itemized fixes. Measurement definitions can be clear while implementation details stay private.

## Synthetic examples

Scenarios under `examples/` are marked **SIMULATED / 合成示例**, use fictional identifiers such as SOURCE_A, SOURCE_B, and ASSET_X, and declare `data_classification: synthetic` in their JSON. This classification applies to synthetic examples; it does not classify measurement aggregates or charts based on them as fictional data.

Examples are authored from scratch, not renamed exports of real logs. They contain no real-format addresses, capital, return, latency, or actual timestamps. Their fields are for this showcase only.

An example may leave a result unresolved. Source intent, request submission, and actual fills are not treated as necessarily identical. Risk categories are not mapped to fixed production actions.

## Combined disclosure

Review prose, figures, data, comments, paths, and historical materials together to prevent files from jointly exposing source identities, internal rules, or deployment clues. The review should protect implementation and identities while retaining enough public evidence to interpret and compare results.

This edition removes interface outline code in favor of concept descriptions. The only programs are generic local validation and packaging utilities.

## History and rights

This ZIP contains no Git history, raw operating data, or production implementation. It cannot erase earlier public history, forks, caches, or downloads. When updating an existing repository, also remove files listed in [REMOVED_FILES.txt](../../REMOVED_FILES.txt); overwriting matching names is insufficient.

[LICENSE](../../LICENSE) reserves rights in new original material while preserving earlier grants. The exact legacy notice is in [LICENSES/LEGACY_LICENSE.txt](../../LICENSES/LEGACY_LICENSE.txt). Previously licensed portions, including reused portions, remain subject to their applicable earlier license. This notice does not remove platform permissions to view or fork, or uses allowed by law.

Public material can still be read and learned from. Protection here comes from limiting implementation disclosure; the documents, license, and checks do not make copying impossible.

Feedback on public metric definitions, documentation, and synthetic scenarios is welcome. Refer to public paths and data without attaching real logs, account records, or private configuration. See [Contributing](../../CONTRIBUTING.md) and [Security](../../SECURITY.md).

Trading involves fill differences, delays, rejected orders, and possible losses. This showcase promises no returns, fill rate, recovery time, or loss-stop outcome.

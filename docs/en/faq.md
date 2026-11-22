# Frequently asked questions

[中文](../faq.md) · [Project home](../../README.en.md) · [Scenario guide](showcase.md)

## About the repository

### What is this repository?

It is the public results showcase for Multisource HL Copy, presenting coordination across sources alongside documented historical performance and validation aggregates. It includes documentation, performance charts, concept illustrations, and static synthetic examples. See [Public scope](public-scope.md) for the boundary between result evidence and the private production implementation.

### Can I start trading after downloading it?

No. The repository has no trading runtime, account integration, key configuration, or deployment entry point. Reading JSON, viewing images, or running the public-material checks does not connect a trading account or submit orders.

### Why describe capabilities without publishing the implementation?

Capability descriptions explain use cases and product trade-offs; historical measurement aggregates show observable engineering results. Latency, burst throughput, concurrent-source counts, and test coverage can be published with the context needed to interpret them while algorithms, operating parameters, and production configuration remain private. Each result applies to its documented version and scope.

### Does a public repository mean that all materials can be used without restriction?

Usage depends on the applicable license, not on whether materials are publicly accessible. Read the root [LICENSE](../../LICENSE) and the historical-license notes it references. Showcase materials do not grant access to private code or services.

## About measurements, illustrations, and synthetic scenarios

### Are the examples real logs with names changed?

The scenarios under `examples/` are not. They are authored from scratch using fictional sources, assets, states, and example values, marked **SIMULATED / 合成示例**, and declare `data_classification: synthetic` in their JSON. The separately published [measurement aggregates](../../benchmarks/results.json) derive from documented historical measurements and are classified as `measured_aggregate`. They are not synthetic scenarios and do not include raw event traces.

### Do SOURCE_A or ASSET_X map to real accounts or assets?

No. They are fictional labels without mappings to real wallets, accounts, markets, or assets. Replacing them with real addresses would not make the examples runnable; the repository provides no such functionality.

### Are the images actual administration screens?

Concept illustrations explain scenarios and information relationships; they are not screenshots of actual administration screens. The [performance chart](../../assets/performance.svg) visualizes published measurement aggregates, with evidence and definitions in [Performance and validation](performance.md). Each image takes its meaning from its data and caption; neither synthetic data nor a live interface is a blanket description of all figures.

### Is the JSON a production API, configuration template, or importable strategy?

No. The [scenario](../../examples/scenario.json), [report](../../examples/report.json), and [risk event](../../examples/risk-event.json) are synthetic reading materials; the [measurement aggregates](../../benchmarks/results.json) store publishable historical metrics. Both classes of JSON are documentation data, not production APIs, executable configuration, or strategy rules.

### Can example values be used to compare performance or returns?

Synthetic values under `examples/` cannot. They explain scenarios without a real measurement basis. Performance analysis should use results classified as `measured_aggregate` together with their measurement boundaries, historical attribution, and known limitations. Those engineering metrics do not themselves measure returns.

## About capabilities and evidence

### Does the feature page prove which capabilities are live?

[Features](features.md) alone describes capabilities. [Performance and validation](performance.md) supplies documented result evidence for the historical scope it explicitly identifies. Historical measurements do not automatically establish that all current-release features are live or have been revalidated.

### What information can public benchmarks contain?

They can contain documented latency percentiles, burst signal throughput, tested concurrent-source counts, test categories, and aggregate counts. Anonymized environment classes, generic measurement start and end boundaries, sample sizes, duration, tested-target counts, and error or drop rates are also publishable. This context helps readers assess where a result applies. Missing records should be acknowledged, never invented. See the [benchmark data guide](../../benchmarks/README.md) and [Verification scope](testing.md).

### How should I interpret p99, burst throughput, and source counts?

p99 must come from the corresponding record; it cannot be inferred from p50 or a mean. Burst throughput in signals/s needs a defined processing layer and measurement window; it is not exchange orders or fills per second. A tested concurrent-source count describes the sources covered by that test, not an automatic maximum. Tested targets, sources, and statistical samples are also different counting units.

### Are these numbers from the latest release?

Use the historical period, version, and validation scope attached to each result. This package preserves the historical status of historical measurements; a documentation update is not an engine retest. New measurements should add or explicitly update the corresponding records with clear version attribution.

### What does the public check script validate?

From the repository root, using Python 3.10 or later, run:

```bash
python3 tools/check_public.py
```

The script checks public files, classifications, references, and disclosure rules; its contents define the specific checks. It helps keep materials consistent. It does not rerun the trading engine or historical measurements, and it does not replace an independent audit.

### If a risk example says an issue was addressed, does that establish that real risk was removed?

No. The example state belongs to a fictional situation. It does not establish that market actions complete on time, create a fixed mapping between real events and actions, or guarantee a loss limit.

## About history, feedback, and reporting

### Does replacing the current ZIP remove material published earlier?

No. Updating current files does not automatically rewrite Git history, existing release attachments, branches, derivative copies, caches, screenshots, or other people's downloads. This package describes only the currently supplied materials and cannot promise that earlier public content has disappeared. Existing applicable license rights also do not cease to exist merely because a ZIP is updated.

### What contributions are welcome?

Improvements to documentation, translation, charts, and synthetic scenarios are welcome, as are documented, sanitized measurement aggregates within the public boundary. Measurements should state their definitions and historical attribution; synthetic scenarios should retain their classification. Do not include production implementations, real configuration, addresses, account records, or logs. See [CONTRIBUTING.md](../../CONTRIBUTING.md).

### Can I post my logs in a public discussion to demonstrate an issue?

Do not submit real logs, account screenshots, credentials, or records identifying sources. A minimal fictional situation is sufficient to explain a documentation issue, and synthetic examples must remain clearly labeled.

### Where should suspected sensitive content be reported?

Follow [SECURITY.md](../../SECURITY.md). Use private vulnerability reporting only if the repository actually has that feature enabled. Otherwise, first request a private communication channel without posting secrets or their detailed locations in public. This repository does not invent a contact email or reporting service.

Related reading: [Performance and validation](performance.md) · [Scenario guide](showcase.md) · [Features](features.md) · [Public showcase roadmap](roadmap.md).

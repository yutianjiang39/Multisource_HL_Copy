# Frequently asked questions

[中文](../faq.md) · [Project home](../../README.en.md) · [Scenario guide](showcase.md)

## About the repository

### What is this repository?

It is the public showcase package for Multisource HL Copy, describing the problems the product addresses, how capabilities are presented, and the reading experience. It contains documentation, conceptual illustrations, and static synthetic examples. Its scope differs from the private production implementation; see [PUBLIC_SCOPE.md](../../PUBLIC_SCOPE.md).

### Can I start trading after downloading it?

No. The repository has no trading runtime, account integration, key configuration, or deployment entry point. Reading JSON, viewing images, or running the public-material checks does not connect a trading account or submit orders.

### Why describe capabilities without publishing the implementation?

Capability descriptions help visitors understand use cases, observable outcomes, and product trade-offs without exposing execution algorithms, specific parameters, or operating environments. Readers can discuss whether those descriptions are complete. They cannot establish from the descriptions alone that the private system implements or has verified the capabilities.

### Does a public repository mean that all materials can be used without restriction?

Usage depends on the applicable license, not on whether materials are publicly accessible. Read the root [LICENSE](../../LICENSE) and the historical-license notes it references. Showcase materials do not grant access to private code or services.

## About illustrations and synthetic data

### Are the examples real logs with names changed?

No. The situations, sources, assets, states, and values in this showcase were constructed to explain concepts. They are not renamed real logs or anonymized exports from real accounts. They are explicitly marked **SIMULATED / 合成示例**.

### Do SOURCE_A or ASSET_X map to real accounts or assets?

No. They are fictional labels without mappings to real wallets, accounts, markets, or assets. Replacing them with real addresses would not make the examples runnable; the repository provides no such functionality.

### Are the images actual administration screens?

No. They are explanatory illustrations created for the public introduction, showing processes and information relationships. They do not establish that a corresponding web console exists or that the depicted states come from a running service.

### Is the JSON a production API, configuration template, or importable strategy?

No. The [scenario](../../examples/scenario.json), [report](../../examples/report.json), and [risk event](../../examples/risk-event.json) are reading materials. Their field names and structures do not promise compatibility with a production interface, and they are not executable configuration or strategy rules.

### Can example values be used to compare performance or returns?

No. Synthetic values serve presentation and readability without a real measurement basis. They cannot establish actual following quality, latency, availability, returns, or risk, and cannot support selecting real trading sources.

## About capabilities and evidence

### Does the feature page prove which capabilities are live?

No. [Features](features.md) contains capability descriptions; illustrations and examples demonstrate presentation. Establishing whether private features are implemented, deployed, or live-verified requires separate evidence tied to a specific version, environment, and evaluation scope.

### Why are production test counts and performance benchmarks absent?

The current public package does not provide them. **Omission neither disproves them nor verifies them through this package.** Whatever conclusion someone reaches about earlier figures, current synthetic examples cannot replace the original evidence. See [Verification scope](testing.md) for the boundaries of public evidence.

### What does the public check script validate?

From the repository root, using Python 3.10 or later, run:

```bash
python3 tools/check_public.py
```

The script checks the public showcase package itself; its contents define the specific checks. It is not a trading-engine test, backtest, live experiment, or security audit. Passing it does not establish correct trade execution, credential safety, effective risk controls, or real report values.

### If a risk example says an issue was addressed, does that establish that real risk was removed?

No. The example state belongs to a fictional situation. It does not establish that market actions complete on time, create a fixed mapping between real events and actions, or guarantee a loss limit.

## About history, feedback, and reporting

### Does replacing the current ZIP remove material published earlier?

No. Updating current files does not automatically rewrite Git history, existing release attachments, branches, derivative copies, caches, screenshots, or other people's downloads. This package describes only the currently supplied materials and cannot promise that earlier public content has disappeared. Existing applicable license rights also do not cease to exist merely because a ZIP is updated.

### What contributions are welcome?

Improvements to documentation, translation, illustration readability, and entirely fictional scenarios are welcome. Contributions should help visitors understand capabilities and limitations without adding production implementations, real configuration, addresses, account records, or logs. See [CONTRIBUTING.md](../../CONTRIBUTING.md).

### Can I post my logs in a public discussion to demonstrate an issue?

Do not submit real logs, account screenshots, credentials, or records identifying sources. A minimal fictional situation is sufficient to explain a documentation issue, and synthetic examples must remain clearly labeled.

### Where should suspected sensitive content be reported?

Follow [SECURITY.md](../../SECURITY.md). Use private vulnerability reporting only if the repository actually has that feature enabled. Otherwise, first request a private communication channel without posting secrets or their detailed locations in public. This repository does not invent a contact email or reporting service.

Related reading: [Scenario guide](showcase.md) · [Features](features.md) · [Public showcase roadmap](roadmap.md).

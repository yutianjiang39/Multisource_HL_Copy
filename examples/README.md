# 合成样例 / Synthetic examples

[返回首页](../README.md) · [English home](../README.en.md)

这些文件从空白构造，用于解释展示内容。它们不是真实记录的改名版本，不是交易模拟器输入，也不是生产 API、配置或内部事件格式。

Every file is authored from scratch for this showcase. It is not a renamed real record, simulator input, production API, configuration, or internal event contract.

| 文件 / File | 用途 / Purpose |
| --- | --- |
| [scenario.json](scenario.json) | 来源意图、本方观察与待确认事项 / Source intent, observations, and open questions |
| [report.json](report.json) | 多来源摘要与定性报告 / A qualitative multi-source report |
| [risk-event.json](risk-event.json) | 风险说明、已知事实与人工关注项 / Risk communication and review items |

## 阅读字段 / Field guide

| 字段 / Field | 含义 / Meaning |
| --- | --- |
| data_classification | 固定为 synthetic / Always synthetic |
| display_type | 固定为 illustration_only / Always illustration_only |
| example_id | 仅在公开示例内使用的 DEMO 标记 / A showcase-only DEMO label |
| label | 显著的合成标记 / Prominent synthetic label |
| source_id / asset_id | SOURCE_A、ASSET_X 等虚构符号 / Fictional symbols |
| title / description | 中英文说明 / Chinese and English copy |
| steps / observations / review_items | 阅读结构，不代表真实调度或处置规则 / Presentation structure, not execution rules |

不含地址、密钥、真实时间戳、价格、数量、比例、收益、时延或生产阈值。步骤顺序是叙述顺序；状态词是公开说明文字，不对应私有状态枚举。

No addresses, keys, real timestamps, prices, sizes, ratios, returns, latency, or production thresholds are included. Steps are narrative ordering; status words are presentation vocabulary, not private enums.

## 与图示的关系 / Relationship to figures

[场景导览](../docs/showcase.md) 和 [English guide](../docs/en/showcase.md) 提供解释；SVG 采用同样的虚构对象和定性描述。图示是静态插图，不从 JSON 驱动交易或执行状态更新。

The scenario guides explain the same fictional objects and qualitative states used in the SVGs. The illustrations are static and do not turn JSON into trading actions or state updates.

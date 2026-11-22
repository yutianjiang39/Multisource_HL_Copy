# 性能数据与测量口径 / Performance data and methodology

[中文性能页](../docs/performance.md) · [English performance](../docs/en/performance.md) · [results.json](results.json)

本目录的数字是**真实记录的脱敏汇总**，分类为 `measured_aggregate`。它与 [examples/](../examples/README.md) 中的合成场景不同。

These are sanitized summaries of recorded measurements and documented limits, classified as `measured_aggregate`. They are distinct from the fictional examples.

## 证据来源 / Evidence basis

结果来自项目保留的历史主网样本汇总、模拟验收记录、运行摘要，以及提供版本的配置校验。原始账户信息、逐笔记录、运行位置、版本散列和生产配置不随包发布。这一版整理公开证据，没有重新压测，也不是第三方审计。

The source material consists of retained mainnet aggregates, simulated acceptance summaries, run summaries, and configuration validation in the supplied version. Raw account details, events, operating locations, commit hashes, and production configuration are not distributed. This edition organizes existing evidence; it is not a fresh benchmark or an independent audit.

## 记录索引 / Record index

| ID | 指标 / Metric | 类型 / Kind |
| --- | --- | --- |
| PERF-LIVE-LOCAL | 本地提交分位数 / Local submission percentiles | 主网历史观察 / Historical mainnet |
| PERF-LIVE-FEED | 来源信号传播 / Source signal delivery | 主网历史观察 / Historical mainnet |
| PERF-LIVE-INCLUSION | 本方订单入块 / Follower order inclusion | 主网历史观察 / Historical mainnet |
| PERF-LIVE-CANCEL | 本方撤单入块 / Cancellation inclusion | 主网历史观察 / Historical mainnet |
| PERF-BURST-TWO | 双来源 150/s 脉冲 / Two-source 150/s bursts | 模拟验收 / Simulated acceptance |
| PERF-TARGET-CONFIG | 最多 8 个可配置目标 / Up to eight configured targets | 配置上限 / Configuration limit |
| PERF-TARGET-DRYRUN | 5 目标演练 / Five-target rehearsal | 真实数据、模拟执行 / Live data, simulated execution |
| PERF-TARGET-LIVE | 3 目标实盘 / Three-target session | 历史运行摘要 / Historical run summary |
| PERF-SHADOW-PLACE | 端到端委托生效 / End-to-end order effectiveness | 脚本来源主网测试 / Scripted-source mainnet test |
| PERF-SHADOW-CANCEL | 端到端撤单生效 / End-to-end cancellation | 脚本来源主网测试 / Scripted-source mainnet test |

## 如何读取 / Reading the fields

- `measurement_boundary`：计时或计数的起止定义 / The measurement boundary.
- `unit`：单位；脉冲记录的主单位是 signals/s，扩展字段用名称明确 ms、秒或百分比 / Main unit; supplementary fields name their own units.
- `sample_count`：延迟记录为有效样本数；脉冲记录为轮次。未保留的不补写 / Valid samples for latency, run count for bursts; absent when unavailable.
- `values`：数值结果；各轮 p99 范围与合并 p99 分开 / Results; a range of per-run p99s is not a pooled p99.
- `conditions` 与 `limitations`：实验条件和适用边界 / Conditions and applicability.
- `version_scope`：历史记录或所提供配置，不暗示最新版重测 / Historical measurement or supplied configuration, not latest-build revalidation.

## 发布规则 / Publication rules

可以公开结果、分位数、有效样本数、测试窗口、匿名环境等级、错误率和测试过的目标数。必须说明这些数字量到了哪一层。

Publish outcomes, percentiles, sample sizes, windows, anonymous environment classes, error rates, and tested target counts with their measured layer.

不通过相加分位数产生端到端 p99，不把接收帧率写成下单率，不把短脉冲写成持续满载，不把配置目标数写成实测极限。没有保留的指标不凭空填补。

Do not add segment percentiles, equate ingestion with order throughput, turn short bursts into sustained capacity, or present a configured count as a measured maximum. Do not invent missing metrics.

查看、校验这些数据无需交易账户。仓库检查只核对文件结构、必需口径与常见敏感模式；无法独立验证私有实验或检测所有误导性表述。

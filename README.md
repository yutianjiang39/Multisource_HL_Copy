# Multisource HL Copy

**面向 Hyperliquid 的多来源跟单执行引擎**

事件驱动 · Rust 实时执行 · 多目标跟随 · 风险与运行可观测性

[![公开文件检查状态](https://img.shields.io/github/actions/workflow/status/yutianjiang39/Multisource_HL_Copy/public-check.yml?style=flat-square&label=checks&labelColor=161B22)](https://github.com/yutianjiang39/Multisource_HL_Copy/actions/workflows/public-check.yml)
[![Star 数](https://img.shields.io/github/stars/yutianjiang39/Multisource_HL_Copy?style=flat-square&color=3FB8AF&labelColor=161B22)](https://github.com/yutianjiang39/Multisource_HL_Copy/stargazers)
[![最新展示版本](https://img.shields.io/github/v/tag/yutianjiang39/Multisource_HL_Copy?style=flat-square&label=showcase&color=3FB8AF&labelColor=161B22)](RELEASES.md)
![Rust](https://img.shields.io/badge/Rust-161B22?style=flat-square&logo=rust&logoColor=DEA584)
![Python](https://img.shields.io/badge/Python-161B22?style=flat-square&logo=python&logoColor=3776AB)

一个执行账户关注多个来源，覆盖委托跟随、仓位变化、风险干预和运行报告。项目围绕低本地处理开销、突发信号承载和多来源运行组织执行能力。

![性能摘要：23 ms 本地提交 p99、150 条信号每秒脉冲测试、8 个可配置目标。不同数字的证据范围分别标注。](assets/performance.svg)

## 性能快照

| 优势 | 已记录结果 | 口径 |
| --- | --- | --- |
| **低本地提交延迟** | **p99 23 ms · p50 14 ms** | 1,765 笔主网订单样本，收到信号至记录提交时点 |
| **突发信号承载** | **双来源合计 150 条/秒** | 每轮 3 段 × 5 秒，10 轮模拟验收全部通过 |
| **多目标配置** | **最多 8 个目标** | 配置内去重后总数，包含主目标；不作为满载容量声明 |
| **多来源验证** | **3 目标实盘 · 5 目标演练** | 分别约 144h 主网运行与约 144h 真实数据演练 |
| **端到端主网观察** | **委托 0.51 秒 · 撤单 0.47 秒** | 小额脚本来源测试的中位数；分别 73 / 69 个样本 |


| 场景 |  p50 / p90 |
| --- | ---: |
| 单笔挂单  | **429 / 552 ms** |
| 50 笔批量挂单  | **469 / 588 ms** |
| 最快一笔  | **355 ms** |

这些是 2026 年 11 月项目历史记录的脱敏摘要，不是虚构展示数字。不同测试对应不同版本、负载与时间边界；23 ms 不包含交易所确认，150/s 是短脉冲输入速率。完整条件、统计范围与未测项目见 [性能与规模](docs/performance.md) 。

## 系统能力

| 能力 | 对使用者的价值 |
| --- | --- |
| **多来源跟随** | 在同一执行账户中组织多个来源，保留来源上下文与结果说明 |
| **委托生命周期** | 覆盖挂单镜像、委托变更、撤销与对应执行状态 |
| **成交与仓位变化** | 吃单开仓、跟随减仓及剩余仓位处理形成完整的跟随链路 |
| **运行控制** | 围绕启动、停止、配置变化与来源调整组织操作体验 |
| **风险干预** | 提供风险判断、暂停或停止、撤单与平仓等能力，并保留结果和未决状态 |
| **报告与追踪** | 用事件提醒、周期报告与运行记录帮助理解执行结果 |

功能细节见 [功能说明](docs/features.md)。能力说明不构成所有场景下成交、恢复或损失控制的保证。

## 工程优势

**Rust 负责实时执行，Python 负责控制与报告。** 执行链路以事件驱动组织，低延迟路径与操作、报告逻辑职责分离，边界清晰。

**性能以分位数和负载条件表述。** 本地提交、模拟脉冲与主网端到端三类指标分开呈现，每个数字都注明口径，不用单一峰值概括整体表现。

**多来源能力有分层证据支撑。** 配置上限、真实数据演练、主网运行与模拟压力测试各自界定适用范围，扩展能力有据可查，而不是笼统宣称。

**覆盖完整运行闭环。** 系统不止于发出订单请求，还涵盖状态观察、风险干预、运行控制与报告追踪。


> 这是公开展示仓库。生产交易实现保持私有；包内没有账户接入、签名或交易运行时。

## 阅读导航

| 想了解什么 | 从这里开始 |
| --- | --- |
| 实际记录的延迟、负载与目标规模 | [性能与规模](docs/performance.md)|
| 系统提供哪些能力 | [功能说明](docs/features.md)|
| 更多问题 | [FAQ](docs/faq.md)、[版本记录](RELEASES.md) |



工具只处理公开文件，不连接交易账户。维护规则见 [维护公开版](docs/maintaining-public.md)。欢迎按 [贡献说明](CONTRIBUTING.md) 提出文档、测量口径或展示建议。

## 公开边界与许可

性能结果、必要测试条件与工程能力可以公开；执行算法、策略参数、真实身份、原始交易及部署访问细节不公开，见 [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md)。

使用条件见 [LICENSE](LICENSE)；旧版已授予的许可继续适用于对应材料。项目不构成收益承诺。Hyperliquid 名称用于说明项目关注的平台，不代表官方合作或背书。

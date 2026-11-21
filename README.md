# Multisource HL Copy

**一个执行账户，同时跟随多个 Hyperliquid 来源钱包的永续合约委托：按比例镜像挂单、跟随减仓与吃单开仓，并在异常时暂停、撤单或平仓。**

> 这是项目的**展示仓库**：介绍系统做什么、效果怎样、验证到了哪一步。生产实现（Python 控制层 + Rust 执行引擎）保存在私有仓库，这里没有可运行的交易程序。范围说明见 [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md)。

![一次正常跟随：来源动作 → 系统响应 → 最终状态（示意数据）](assets/follow_flow.svg)

## 重点能力

| 能力 | 一句话 |
|---|---|
| **多来源跟单** | 一个账户跟多个来源；同一个币同一时间只归一个来源，冲突时先到先得，其余来源在这个币上的信号被屏蔽并记录 |
| **订单全程跟随** | 挂单、改价、撤单、部分成交、来源减仓与清仓、本方残仓清理，都有对应动作；结果不明的委托不会被重发 |
| **风险控制** | 交易程序内实时计算净值回撤，外部独立守护进程再兜一层；不同风险事件分别执行暂停新增、撤单保仓或平仓 |
| **运行报告与提醒** | 开平仓、保证金、回撤、跟单异常实时推送；定时报告汇总复刻度、延迟、盈亏和需要关注的事项 |

另外还有运行中调参与切换来源、断线与异常恢复、dry_run 演练、滚动事故记录，见 [功能说明](docs/features.md)。

## 有限实测（2026-11-16，主网小额账户）

用脚本控制的测试钱包作来源，跟单实例在主网实盘运行，所有延迟都按交易所时间戳计算：

- 9 类场景（远价挂单、快速撤单、改价、1 秒内 50 张批量挂单、多档挂单、成交、吃单开仓、减仓清仓、范围外不跟）两轮均按设计执行，没有遗留挂单，本地状态与交易所一致。
- 端到端（来源生效 → 镜像生效）中位数：下单约 **0.81 s**，撤单约 **0.67 s**。其中本程序约 0.2 s，其余是交易所确认时间。

适用条件和没有覆盖到的部分见 [效果展示](docs/showcase.md)：单来源、每单约 $11、每轮约 5 分钟，不能外推到所有钱包和行情。

## 阅读入口

| 页面 | 内容 |
|---|---|
| [docs/features.md](docs/features.md) | 8 个功能主题：场景、效果、限制 |
| [docs/showcase.md](docs/showcase.md) | 3 个代表场景与实测结果 |
| [docs/overview.md](docs/overview.md) | 系统由哪几部分组成，各管什么 |
| [docs/roadmap.md](docs/roadmap.md) | 已具备、正在完善、计划探索 |
| [outline/](outline/) | 3 个说明模块职责的示意代码，不是生产实现 |

## 常见问题

**能直接运行吗？** 不能。这里只有说明材料和示意代码，生产程序、配置和部署脚本都不公开。

**哪些内容保持私有？** 执行与恢复的实现、策略参数与阈值、来源钱包的选择与研究、账户与服务器信息、真实日志和记录。详见 [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md)。

**怎么反馈？** 欢迎在 Issues 里提功能建议、指出展示内容的错误或讨论需求。请不要贴自己的私钥、地址余额或部署细节。

## English summary

Multisource HL Copy is a copy-trading system for Hyperliquid perpetuals: one execution account follows several source wallets, mirroring resting orders proportionally, following reduces and taker opens, and pausing, cancelling or flattening on risk events. This is a **showcase repository** with documentation, illustrative diagrams and outline code only; the production implementation (Python control layer + Rust execution engine) is private. A limited mainnet test on 2026-11-16 (single scripted source, ~$11 orders) measured a median end-to-end mirror latency of about 0.81 s for placing and 0.67 s for cancelling, of which about 0.2 s is this system and the rest is exchange confirmation.

## 许可

文字与图片采用 CC BY 4.0，`outline/` 示意代码采用 MIT，见 [LICENSE](LICENSE)。私有仓库里的生产实现不在许可范围内。

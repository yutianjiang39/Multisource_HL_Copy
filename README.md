# Multisource HL Copy

**面向 Hyperliquid 的多来源交易执行项目 · 公开展示版**

把来源意图、执行结果和需要关注的风险，组织成可以理解的运行视图。

[English](README.en.md) · [功能说明](docs/features.md) · [场景导览](docs/showcase.md) · [系统概览](docs/overview.md) · [证据与边界](docs/testing.md) · [常见问题](docs/faq.md)

![多来源、执行关注与运行可见性。概念示意，不是生产架构图。](assets/overview.svg)

> 这里展示项目的能力范围、产品思路和合成场景。生产交易实现保持私有；本仓库不能连接账户或执行交易。图片、场景和数据样例均为独立构造的展示材料，不是实盘记录。

## 项目关注什么

当一个执行账户关注多个来源时，使用者需要持续理解：当前看到了哪些来源变化，执行端有哪些结果，哪些情况仍需核实，以及哪些风险需要人工关注。

Multisource HL Copy 以这些问题组织交易执行、运行控制和报告体验。公开材料保留产品层面的解释，把执行算法、决策规则和部署信息留在私有边界内。

## 能力地图

下表是项目能力主题的介绍，不是本公开包完成实盘验证的声明。

| 主题 | 使用者关心的问题 | 本仓库如何呈现 |
| --- | --- | --- |
| 多来源观察 | 如何分别理解多个来源的活动与当前状态？ | 匿名来源卡片与并列场景 |
| 委托跟随 | 如何看清来源意图变化与本方结果？ | 创建、变更、结束的概念示例 |
| 仓位变化 | 如何识别仓位相关变化和待核实事项？ | 定性状态说明，不提供定量规则 |
| 运行控制 | 如何了解运行状态、操作范围与结果？ | 控制体验的职责说明 |
| 风险可见性 | 哪些事实已确认、哪些还未知？ | 风险提示与人工关注示例 |
| 运行报告 | 本周期有什么变化，下一步关注什么？ | 合成报告与字段说明 |

完整说明见 [功能说明](docs/features.md)。场景结局是人为编排的说明，不代表来源订单一定会被跟随、成交或以相同价格成交。

## 三分钟浏览

1. 看 [场景导览](docs/showcase.md)：理解委托变化、多来源观察、风险提示和周期报告。
2. 看 [系统概览](docs/overview.md)：了解职责边界与产品取舍，不涉及内部调度。
3. 看 [证据与边界](docs/testing.md)：区分能力描述、合成示例和真正的验证证据。
4. 看 [公开范围](PUBLIC_SCOPE.md)：了解本版包含什么，以及哪些内容继续保持私有。

![来源意图、本方观察和待确认事项。全部为合成内容。](assets/follow_flow.svg)

## 可以在本地做什么

直接阅读 Markdown、打开 SVG，或查看 [合成数据样例](examples/README.md)。只验证、打包本展示仓库时，使用 Python 3.10 或更高版本：

```bash
python3 tools/check_public.py
python3 tools/package_public.py --output ../Multisource_HL_Copy-public.zip
```

这两个工具只处理本地展示文件。没有交易 SDK、账户配置、密钥输入、网络查询或下单功能。GitHub 工作流也只运行展示文件检查。

## 内容导航

| 入口 | 内容 |
| --- | --- |
| [功能说明](docs/features.md) / [English](docs/en/features.md) | 产品能力、适用场景和限制 |
| [场景导览](docs/showcase.md) / [English](docs/en/showcase.md) | 四组独立构造的展示旅程 |
| [系统概览](docs/overview.md) / [English](docs/en/architecture.md) | 高层职责与可观察结果 |
| [证据与边界](docs/testing.md) / [English](docs/en/testing.md) | 什么能从本仓库验证，什么不能 |
| [常见问题](docs/faq.md) / [English](docs/en/faq.md) | 运行、数据、使用与反馈 |
| [路线图](docs/roadmap.md) / [English](docs/en/roadmap.md) | 公开展示材料的改进方向 |
| [维护公开版](docs/maintaining-public.md) | 内容校验、发布清单与历史边界 |
| [公开范围](PUBLIC_SCOPE.md) / [English](docs/en/public-scope.md) | 披露边界与许可说明 |
| [版本记录](RELEASES.md) | 只记录公开材料的变化 |

## 反馈与使用边界

欢迎提出文案、图示、翻译和产品表达方面的建议。请按 [贡献说明](CONTRIBUTING.md) 提交不含账户或部署信息的反馈；涉及敏感内容请先阅读 [安全反馈](SECURITY.md)。

本版新增原创内容保留权利；此前已授予的许可继续适用于相应材料。完整范围见 [LICENSE](LICENSE) 和 [旧许可记录](LICENSES/LEGACY_LICENSE.txt)。公开展示不等于生产实现开源，也不构成收益承诺。Hyperliquid 名称用于说明项目关注的平台，不代表官方合作或背书。

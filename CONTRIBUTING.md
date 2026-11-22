# 贡献指南 / Contributing

[中文](#中文) · [English](#english)

## 中文

感谢帮助改进公开展示材料。本仓库接受的改进围绕文档、翻译、性能口径和合成体验示例展开；它不接受私有交易系统的实现贡献，也不是生产问题的日志收集入口。

### 适合提交的改进

- 修正文档中含糊、不一致或不完整的描述。
- 改善中英文对应、术语、导航和图片替代文本。
- 提升概念图与报告示意的可读性。
- 添加完全虚构的场景，帮助理解来源、动作、状态与结果。
- 修正公开样例之间的明显不一致，同时保留其合成性质。
- 补充经过披露审阅的性能汇总，说明分位数、样本、负载、测量边界与版本范围。

提出建议时，请说明访问者遇到了什么阅读问题，以及你的修改怎样帮助理解。

### 保持公开边界

贡献应遵循 [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md)。不要加入：

- 私有源代码、执行算法、策略参数或内部操作步骤。
- 真实账户、钱包地址、来源身份、持仓或余额。
- 凭据、访问令牌、连接端点、部署配置或运行路径。
- 生产日志、真实截图、逐笔记录或真实数据的重命名版本。
- 无公开依据的实盘状态、测试统计、性能或安全承诺。

合成例子应从虚构情境出发，使用 SOURCE_A、SOURCE_B、ASSET_X、ASSET_Y 等标签，并显式标注 **SIMULATED / 合成示例**。不要将真实记录改名后称为合成例子，也不要把展示 JSON 扩展为可执行的账户配置。

### 建议的修改流程

1. 说明要改善的页面、读者问题和预期效果。
2. 修改相关中英文材料，使能力描述与限制条件保持对应。
3. 如果涉及例子，同步检查相关文字、图示与合成数据。
4. 使用 Python 3.10 或更新版本，在仓库根目录运行公开检查：
   
   ```bash
   python3 tools/check_public.py
   ```
5. 人工阅读修改后的内容，确认标签清楚、链接有意义，并且没有加入原始运行记录或敏感细节。经过整理的真实统计按 measured_aggregate 单独标注。
6. 在提交说明中概括修改原因、涉及文件和公开检查结果。

公开检查只覆盖脚本定义的展示包检查项。检查通过不代表交易程序经过测试，也不替代内容复核。不要为展示改进引入账户访问、联网采集或交易操作。

### 文字与示例的表达原则

能力说明应回答“关注什么问题、读者能看到什么、有哪些限制”。图示中的动作不等于真实执行成功，虚构数值不等于测量结果。未知或未提供的信息应保持明确，不能用推测补成已验证事实。

如果讨论历史数据或旧版本公开材料，应准确区分“本包不再提供”与“历史内容不存在”。更新当前材料不会自动删除已经公开的其他副本。

### 使用条件与敏感内容

只提交你有权公开的内容；复用材料时说明来源与适用条件。相关许可见 [LICENSE](LICENSE) 及其中引用的历史许可文件。

发现疑似敏感内容时，不要在公开 Issue 或 Pull Request 中贴出秘密或详细证据。请按 [SECURITY.md](SECURITY.md) 先寻找合适的私下报告渠道。

## English

Thank you for helping improve the public showcase. Contributions focus on documentation, translation, measurement definitions, and synthetic experience examples. This repository does not accept implementations of the private trading system and is not an intake channel for production logs.

### Suitable contributions

- Clarify ambiguous, inconsistent, or incomplete descriptions.
- Improve Chinese–English alignment, terminology, navigation, and image alternative text.
- Improve the readability of conceptual diagrams and report illustrations.
- Add entirely fictional scenarios that explain sources, actions, states, and outcomes.
- Correct clear inconsistencies between public examples while preserving their synthetic nature.
- Add disclosure-reviewed performance summaries with percentiles, samples, workload, measurement boundaries, and version scope.

When suggesting a change, explain the reader's difficulty and how the change improves understanding.

### Preserve publication boundaries

Follow [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md). Do not add:

- Private source code, execution algorithms, strategy parameters, or internal operating procedures.
- Real accounts, wallet addresses, source identities, positions, or balances.
- Credentials, access tokens, connection endpoints, deployment configuration, or operational paths.
- Production logs, real screenshots, individual trading records, or renamed versions of real data.
- Unsupported live-operation claims, test statistics, performance claims, or safety commitments.

Construct synthetic examples from fictional situations. Use labels such as SOURCE_A, SOURCE_B, ASSET_X, and ASSET_Y, and explicitly mark them **SIMULATED / 合成示例**. Renaming real records does not make them synthetic. Do not turn showcase JSON into executable account configuration.

### Suggested workflow

1. Identify the page, the reader's problem, and the intended improvement.
2. Update the related Chinese and English materials, keeping capabilities and limitations aligned.
3. For example changes, check the associated prose, illustrations, and synthetic data together.
4. With Python 3.10 or later, run the public check from the repository root:
   
   ```bash
   python3 tools/check_public.py
   ```
5. Read the changed materials manually to confirm clear labels, meaningful links, and the absence of raw operational records or sensitive details. Curated real aggregates are separately labeled measured_aggregate.
6. Summarize the reason for the change, the affected files, and the public-check result in the submission.

The public check covers only the showcase checks defined by the script. Passing it does not mean that a trading program was tested and does not replace content review. Do not introduce account access, network collection, or trading actions for a showcase improvement.

### Writing and example principles

Capability descriptions should explain the problem, what a reader can observe, and the limitations. An illustrated action is not evidence of successful real execution, and fictional values are not measurements. Keep unknown or missing information explicit instead of filling gaps with speculation presented as verified fact.

When discussing historical data or older public materials, distinguish “not provided in this package” from “does not exist historically.” Updating current materials does not automatically delete other copies already made public.

### Usage terms and sensitive content

Submit only material you have the right to publish. Identify sources and applicable terms when reusing content. See [LICENSE](LICENSE) and the historical-license files it references.

If you find suspected sensitive content, do not post secrets or detailed evidence in a public Issue or Pull Request. Follow [SECURITY.md](SECURITY.md) to establish an appropriate private reporting channel first.

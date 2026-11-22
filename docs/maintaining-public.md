# 维护与发布公开版 / Maintaining the showcase

[中文首页](../README.md) · [English home](../README.en.md)

## 维护目标

公开材料应清楚呈现产品价值与工程成绩。新增内容优先回答：解决了什么问题、实际测得什么、结果适用于什么范围。可以公开真实、脱敏的聚合指标，同时保护算法、操作参数、来源身份与生产配置。

## 维护两类数据

| 类别 | 位置与用途 | 维护要求 |
| --- | --- | --- |
| `measured_aggregate` | `benchmarks/results.json`、性能文档与相应图表；展示有记录依据的历史测量结果 | 保留结果原有口径、单位、历史归属和已知限制；仅发布脱敏汇总 |
| `synthetic` | `examples/`；解释场景和阅读方式 | 从空白构造并标记 **SIMULATED / 合成示例**；不改名导出私有日志 |

不要把所有 JSON、图片或数值统一写成合成数据。性能图表应与测量记录一致；概念图和场景样例应明确各自用途。私有配置、原始截图、事件轨迹与修复细节不进入公开版。

## 新增测量结果

1. 确认数字有记录依据，保留其测量定义与历史归属。未记录的版本、环境或统计条件明确标为未记录，不自行补造。
2. 公开理解结果所需的背景：通用测量起止边界、匿名化环境类别、样本量、持续时间、被测来源或目标数，以及可用的错误率或丢弃率及其分母。测试类别与汇总测试数量也可以公开。
3. 保持结论与证据同宽：p99 不能从 p50 推算；实测来源数不是最大容量；突发 signals/s 应说明处理层与测量窗口，不写成交易所吞吐率或持续负载保证。
4. 同步更新中英文性能说明、结构化结果、图表与相关入口。文档更新时间与引擎复测时间分别表达，历史结果不改称最新结果。

用于理解基准的元数据可以公开。需要保护的是执行机制、算法、阈值和操作参数，以及可识别来源、主机、路径、原始轨迹和生产配置的内容。

## 本地检查与打包

使用 Python 3.10 或更高版本，在仓库根目录执行：

```bash
python3 tools/check_public.py
python3 tools/package_public.py --output ../Multisource_HL_Copy-public.zip
```

[public-files.txt](../public-files.txt) 是明确的发布清单。新增公开文件时人工确认用途与披露范围，再更新清单。清单不是“所有当前文件都可以发布”的自动批准。

检查器允许正常克隆仓库的根 Git 元数据目录存在，但打包器只取清单文件，归档中不包含历史。Python 自身生成的字节码缓存不作为公开文件打包。其他未列入清单的文件会使检查失败，而不是静默带入归档。

输出放在仓库外。默认打包路径也位于仓库外。相同内容生成的归档按固定路径顺序、时间戳和权限打包，方便核对；这不构成内容安全保证。

## 更新现有公开仓库

1. 对照新工作树更新公开文档、测量汇总、图示、样例与工具。
2. 同时删除 [REMOVED_FILES.txt](../REMOVED_FILES.txt) 中的旧文件；仅覆盖同名文件会留下已移除的接口轮廓。
3. 本地检查通过后，人工复读所有变更，确认结果与证据一致，并检查跨文件组合后是否披露了内部机制、身份或部署线索。
4. 在自己的正常发布流程中查看差异，再提交或上传。这个包本身不会推送远端、改写历史或发布网站。

旧提交、分叉、发布附件与既有下载不因替换当前工作树而消失。如需处理此前披露的历史，单独确认范围和处理方案；不要把当前检查通过当成历史已清理的证明。

## 人工复读重点

- 文字、图片与 JSON 是否正确区分测量汇总和合成样例，相关数值、单位与来源是否一致。
- 是否把设计目标写成测量结果、历史测量写成最新复测，或把实测数量写成容量上限。
- 是否明确统计单位、测量边界、样本量、持续时间和记录缺口；p99、突发吞吐率与错误率是否有对应口径。
- 是否出现真实身份、账户、资金、主机、路径、原始事件轨迹、操作参数或内部接口。
- 图示是否暗示来源动作必然产生本方成交。
- 许可与署名是否保留，旧许可权利是否被错误表述为失效。
- 中英文是否表达相同的能力边界与不确定性。

## English guide

### Maintenance goal

Present product value and engineering results clearly: what problem is addressed, what was measured, and where the result applies. Real, sanitized aggregates can be public while algorithms, operating parameters, source identities, and production configuration stay private.

### Maintain two data classes

| Class | Location and purpose | Maintenance rule |
| --- | --- | --- |
| `measured_aggregate` | `benchmarks/results.json`, performance documents, and associated charts; documented historical measurement results | Preserve definitions, units, historical attribution, and known limitations; publish sanitized aggregates only |
| `synthetic` | `examples/`; scenario and reading examples | Author from scratch and label **SIMULATED / 合成示例**; do not rename private log exports |

Do not classify every JSON file, image, or number as synthetic. Performance charts should match their measurement records; concept illustrations and scenario examples should state their purpose. Keep private configuration, original screenshots, event traces, and fix details out of the public package.

### Add measurement results

1. Verify that records support each number, its definition, and its historical attribution. Mark unrecorded versions, environments, or statistical conditions as unrecorded instead of inventing them.
2. Publish the context needed to interpret results: generic measurement start and end boundaries, anonymized environment classes, sample sizes, duration, tested-source or target counts, and available error or drop rates with their denominators. Test categories and aggregate test counts are also publishable.
3. Keep conclusions within the evidence: do not infer p99 from p50, turn tested source counts into capacity ceilings, or describe burst signals/s as exchange throughput or a sustained-load guarantee. State the processing layer and measurement window.
4. Update both language versions, structured results, charts, and related entry points together. Distinguish documentation updates from engine retests, and preserve the historical status of historical results.

Metadata needed to interpret benchmarks can be public. Protect execution mechanisms, algorithms, thresholds, operating parameters, identifiable sources, hosts, paths, raw traces, and production configuration.

### Local checks and packaging

Run the two commands above using Python 3.10+. [public-files.txt](../public-files.txt) is an explicit publication inventory. Confirm the purpose and disclosure scope of a new file before adding it; the inventory does not automatically approve everything in the tree.

The checker permits normal root Git metadata, but the packager includes only inventory files and no history. Generated Python bytecode is not packaged; other unlisted files fail validation. Keep output outside the source tree, as the default does. Deterministic path order, timestamps, and permissions make archives easier to compare, without guaranteeing content safety.

### Update an existing public repository

1. Update documentation, measurement aggregates, figures, examples, and tools from the new working tree.
2. Also remove old files listed in [REMOVED_FILES.txt](../REMOVED_FILES.txt); overwriting matching names leaves removed interface outlines behind.
3. After local checks, review all changes for consistency with their evidence and for combined disclosure of internal mechanisms, identities, or deployment clues.
4. Review the diff in your usual publication process before committing or uploading. These utilities do not push, publish, or rewrite history.

A new working tree does not clean old commits, forks, release attachments, or downloads. Treat any historical exposure as a separate matter. Passing the local checker is not proof that historical content or all semantic disclosures are absent.

### Human review

- Confirm that prose, images, and JSON distinguish measurement aggregates from synthetic examples and use consistent values, units, and sources.
- Check that design goals are not described as measurements, historical results as current retests, or tested counts as capacity ceilings.
- Check statistical units, boundaries, sample sizes, duration, and missing records, including the definitions behind p99, burst throughput, and error rates.
- Exclude real identities, accounts, capital, hosts, paths, raw event traces, operating parameters, and internal interfaces.
- Avoid diagrams implying that source actions necessarily produce follower fills.
- Preserve licenses and attribution without claiming that earlier license rights have expired.
- Keep the same capability boundaries and uncertainty in both languages.

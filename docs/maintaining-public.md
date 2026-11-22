# 维护与发布公开版 / Maintaining the showcase

[中文首页](../README.md) · [English home](../README.en.md)

## 维护目标

公开材料应更易理解，而不是越来越接近实现说明。新增内容优先回答使用者的问题：功能用于什么场景、如何阅读结果、哪些状态仍未知、公开证据的边界在哪里。

示例应从空白构造。不要把私有日志、配置或截图改名后放进公开版，也不要把私有修复细节搬进公开版本记录。

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

1. 对照新工作树更新公开文档、图示、样例与工具。
2. 同时删除 [REMOVED_FILES.txt](../REMOVED_FILES.txt) 中的旧文件；仅覆盖同名文件会留下已移除的接口轮廓。
3. 本地检查通过后，人工复读所有变更，尤其是跨文件组合后是否披露了规则或真实运行信息。
4. 在自己的正常发布流程中查看差异，再提交或上传。这个包本身不会推送远端、改写历史或发布网站。

旧提交、分叉、发布附件与既有下载不因替换当前工作树而消失。如需处理此前披露的历史，单独确认范围和处理方案；不要把当前检查通过当成历史已清理的证明。

## 人工复读重点

- 文字、图片、JSON 是否一致标记为合成。
- 是否把设计目标写成已验证结果，或把局部状态写成全账户结论。
- 是否出现真实身份、账户、金额、时间、部署信息或内部接口。
- 图示是否暗示来源动作必然产生本方成交。
- 许可与署名是否保留，旧许可权利是否被错误表述为失效。
- 中英文是否表达相同的能力边界与不确定性。

## English guide

Improve explanations of capabilities, scenarios, outcomes, and uncertainty. Do not turn this repository into an implementation manual. Author examples from scratch rather than renaming private exports.

Run the two commands above using Python 3.10+. The inventory is an explicit list of approved public files; adding a name is a deliberate disclosure decision. Normal root Git metadata and generated Python bytecode are not packaged. Other unlisted files fail validation. Output belongs outside the source tree.

When updating an existing repository, remove the former files listed in the removal manifest as well as replacing current files. Review the entire diff and combined disclosure before using your usual publication process. These utilities do not push, publish, or rewrite history.

A new working tree does not clean old commits, forks, release attachments, or downloads. Treat any historical exposure as a separate matter. Passing the local checker is not proof that historical content or all semantic disclosures are absent.

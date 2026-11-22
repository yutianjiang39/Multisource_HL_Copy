# 敏感信息报告 / Reporting sensitive information

[中文](#中文) · [English](#english)

## 中文

本仓库是公开展示材料包，不是可运行的交易服务。本页说明如何报告公开材料中疑似不应公开的内容，不是生产系统安全保障、审计结论或事故处置服务。

### 普通文档问题

表述不清、链接失效、翻译差异或合成例子的展示问题，可以按照 [贡献指南](CONTRIBUTING.md) 反馈。公开反馈只需最小的虚构情境，不需要真实账户信息或运行日志。

### 疑似敏感内容

如果发现疑似凭据、账户信息、私有实现或其他不应公开的内容，请避免在公开 Issue、Pull Request、评论或截图中再次传播。

- **如果仓库确实启用了私密漏洞报告入口，** 使用该入口提交最小必要的说明。不要因为存在本文件，就假定私密报告功能已启用。
- **如果没有已确认的私密入口，** 先向维护者请求私下沟通渠道。公开请求只需说明“希望私下报告疑似敏感内容”，不要同时附上秘密、详细位置或可直接复现暴露的材料。
- 建立私下渠道后，先提供简短的问题描述与最小化上下文；不要粘贴完整凭据、真实账户日志或无关个人信息。

本仓库不在此提供未经确认的联系邮箱，也不声称存在额外的私密报告服务。

### 当前副本与既有公开历史

删除或替换当前文件，不等于已经消除 Git 历史、发布附件、派生副本、缓存、截图或下载中的内容。如果有效凭据可能已经暴露，应通过相关服务的账户安全渠道处理撤销或轮换；不能只依赖删除当前展示文件。

本公开包不承诺可以删除他人已经取得的副本。报告时可以说明你看到的是当前材料还是较早的公开版本，但不要在公开讨论中重新附上敏感材料。

### 范围与承诺

本文件不授权访问真实账户、探测未公开基础设施或测试第三方服务。它也不承诺漏洞赏金、响应期限或修复期限。

公开材料检查脚本用于检查展示包，不是安全审计或凭据有效性检查。许可与公开范围分别见 [LICENSE](LICENSE) 和 [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md)。

## English

This repository is a public showcase package, not a runnable trading service. This page explains how to report content that may not belong in public materials. It is not a production security guarantee, an audit conclusion, or an incident-response service.

### Ordinary documentation issues

Unclear wording, broken links, translation differences, and presentation issues in synthetic examples can be reported under the [contribution guide](CONTRIBUTING.md). A minimal fictional situation is sufficient for public feedback; real account information or operational logs are unnecessary.

### Suspected sensitive content

If you find suspected credentials, account information, private implementation details, or other content that should not be public, avoid redistributing it in public Issues, Pull Requests, comments, or screenshots.

- **If the repository actually has private vulnerability reporting enabled,** use that facility with the minimum necessary explanation. The existence of this file does not mean that private reporting is enabled.
- **If no private facility has been confirmed,** first ask the maintainer for a private communication channel. A public request only needs to say, “I would like to report suspected sensitive content privately.” Do not include secrets, detailed locations, or material that directly reproduces the exposure.
- Once a private channel is established, begin with a short description and minimal context. Do not paste complete credentials, real account logs, or unrelated personal information.

This repository does not provide an unverified contact email or claim that an additional private reporting service exists.

### Current copies and earlier public history

Deleting or replacing current files does not remove content from Git history, release attachments, derivative copies, caches, screenshots, or downloads. If valid credentials may have been exposed, use the relevant service's account-security channels to revoke or rotate them; do not rely only on deleting a current showcase file.

This public package does not promise to remove copies already obtained by others. A report may identify whether the concern involves current materials or an older public version, but sensitive materials should not be reattached in public discussions.

### Scope and commitments

This file does not authorize access to real accounts, probing of unpublished infrastructure, or testing of third-party services. It promises no bounty, response deadline, or remediation deadline.

The public-material check script checks the showcase package. It is not a security audit or a check of credential validity. See [LICENSE](LICENSE) and [PUBLIC_SCOPE.md](PUBLIC_SCOPE.md) for usage terms and publication boundaries.

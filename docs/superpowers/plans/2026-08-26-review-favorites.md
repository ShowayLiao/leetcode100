# 收藏与二刷清单实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 superpowers:subagent-driven-development（推荐）或 superpowers:executing-plans 逐任务实现此计划。步骤使用复选框（`- [ ]`）语法来跟踪进度。

**目标：** 为刷题仓库建立一个由用户口头指令驱动、由 Codex 维护的集中 Markdown 收藏与二刷清单。

**架构：** `sets/review.md` 是收藏记录的唯一数据源，每道题一行，保存收藏日期、题目复习入口、收藏原因和二刷次数。`AGENTS.md` 定义 Codex 识别收藏/取消收藏/完成二刷指令、去重、排序和验证链接的行为规则。

**技术栈：** Markdown、相对链接、PowerShell 文件存在性检查；不新增 Python 依赖，不修改解题代码。

---

## 文件清单

- 创建：`sets/review.md`——集中收藏与二刷记录。
- 修改：`AGENTS.md`——新增收藏与复习清单维护规范。
- 不修改：任何 `problems/**/main.py`、题目测试和仓库工具。

当前工作区不存在 `.git`，因此执行阶段不执行也不伪造 Git commit；完成后报告实际修改文件。

### 任务 1：创建集中复习清单

**文件：**

- 创建：`sets/review.md`

- [ ] **步骤 1：写入清单标题、字段说明和当前收藏记录**

使用以下内容创建文件。表格中的本地链接必须相对于 `sets/review.md`，并同时指向题目、代码和笔记：

```markdown
# 收藏与二刷清单

用于记录值得回看或需要二刷的题目。由 Codex 根据用户指令维护。

| 收藏日期 | 题目与复习入口 | 收藏原因 | 二刷次数 |
|---|---|---|---:|
| 2026-08-26 | [题目](../../../problems/leetcode/0002_add_two_numbers/problem.md) · [代码](../../../problems/leetcode/0002_add_two_numbers/main.py) · [笔记](../../../problems/leetcode/0002_add_two_numbers/notes.md) | 逐位相加、进位处理与序列解包 | 0 |
```

- [ ] **步骤 2：确认清单记录没有重复题目**

运行：

```powershell
$review = 'sets/review.md'
$rows = Select-String -Path $review -Pattern '^\| 20[0-9]{2}-[0-9]{2}-[0-9]{2} \|'
$ids = $rows | ForEach-Object { [regex]::Match($_.Line, 'problems/([^/]+/[^/]+)/').Groups[1].Value }
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { throw 'review.md contains duplicate problem directories' }
```

预期：命令无输出且退出码为 `0`。

### 任务 2：把维护协议写入 AGENTS.md

**文件：**

- 修改：`AGENTS.md`，在 `## Repository conventions` 之后新增 `## Review list workflow`。

- [ ] **步骤 1：加入用户指令到 Markdown 更新的映射**

新增以下规则：

```markdown
## Review list workflow

- 集中复习清单位于 `sets/review.md`，由 Codex 根据用户指令维护。
- 用户说“收藏这题”或同义表达时，新增对应题目；记录当前日期、题目/代码/笔记链接、收藏原因和二刷次数 `0`。
- 用户未提供收藏原因时，根据当前对话提炼一句简短、可迁移的复习重点。
- 同一道题已在清单中时不新增重复行；更新原因时保留首次收藏日期和已有二刷次数。
- 用户说“完成一次二刷”或同义表达时，将对应题目的二刷次数加 `1`。
- 用户说“取消收藏”或同义表达时，删除对应题目行。
- 题目身份以规范化的本地题目目录路径判断；清单按收藏日期降序排列，同日按题号升序排列。
- 每次更新后检查 Markdown 表格列数、二刷次数、重复题目和所有相对链接；不得修改题目代码或测试来完成收藏操作。
```

- [ ] **步骤 2：检查规则与现有仓库约定不冲突**

确认新规则仍遵守以下既有约定：题目源文件和解题代码分离、相对路径从当前 Markdown 文件计算、收藏操作不改变 `main.py` 和测试、日期格式使用 `YYYY-MM-DD`。

### 任务 3：验证 Markdown 链接和文档变更

**文件：**

- 检查：`sets/review.md`
- 检查：`AGENTS.md`

- [ ] **步骤 1：验证当前题目的三个入口存在**

运行：

```powershell
$required = @(
    'sets/review.md',
    'problems/leetcode/0002_add_two_numbers/problem.md',
    'problems/leetcode/0002_add_two_numbers/main.py',
    'problems/leetcode/0002_add_two_numbers/notes.md'
)
foreach ($path in $required) {
    if (-not (Test-Path -LiteralPath $path)) { throw "Missing path: $path" }
}
```

预期：命令无输出且退出码为 `0`。

- [ ] **步骤 2：检查关键维护规则和链接均已落盘**

运行：

```powershell
rg -n "Review list workflow|sets/review\.md|二刷次数|0002_add_two_numbers" AGENTS.md sets/review.md
```

预期：输出包含 `AGENTS.md` 中的工作流规则、`sets/review.md` 中的表头和 LeetCode 2 的三个入口链接。

- [ ] **步骤 3：确认本次变更未触碰解题代码**

运行：

```powershell
Get-FileHash 'problems/leetcode/0002_add_two_numbers/main.py'
```

记录哈希用于确认实现阶段只修改文档；不运行题目测试作为文档变更的通过依据，也不声称产生官方 AC。


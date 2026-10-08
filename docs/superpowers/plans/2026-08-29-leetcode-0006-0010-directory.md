# LeetCode 0006–0010 目录实施计划

> **面向 AI 代理的工作者：** 本计划用于当前会话内联执行。每个题目目录单独完成并立即校验，避免把既有 0005 学习内容混入本批改动。

**目标：** 在保留 0005 的前提下，新增 0006–0010 五个遵循仓库约定的 ACM 空白练习目录。

**方案：** 为每道题写入精简 `problem.md`、可填写的 `notes.md`、0 字节 `main.py` 和三组以上输入输出夹具；最后用结构脚本检查路径、文件大小、测试配对与 0005 未被修改。

**技术栈：** Python 标准库（仅用于验证工具）、UTF-8 Markdown、现有 `tools/run_tests.py` 约定。

---

### 任务 1：建立变更前基线

**文件：** 无新增文件。

- [ ] 确认目标目录 `0006_zigzag_conversion`、`0007_reverse_integer`、`0008_string_to_integer_atoi`、`0009_palindrome_number`、`0010_regular_expression_matching` 均不存在。
- [ ] 记录 0005 现有文件清单与内容摘要，后续只比较其内容未发生变化。
- [ ] 确认不修改 `sets/leetcode_hot100.md`、`tools/` 和仓库级测试。

**验证命令：**

```text
Get-ChildItem problems/leetcode -Directory
Get-FileHash problems/leetcode/0005_longest_palindromic_substring/main.py
```

**预期：** 仅存在 0001–0005；五个目标目录不存在；得到 0005 基线哈希。

### 任务 2：创建 0006 字形变换目录

**文件：**

- 创建 `problems/leetcode/0006_zigzag_conversion/problem.md`
- 创建 `problems/leetcode/0006_zigzag_conversion/notes.md`
- 创建空文件 `problems/leetcode/0006_zigzag_conversion/main.py`
- 创建 `tests/01.in`、`tests/01.out`、`tests/02.in`、`tests/02.out`、`tests/03.in`、`tests/03.out`

- [ ] 在题面中写明两行输入（`s`、`num_rows`）、逐行读取输出和长度/行数约束。
- [ ] 测试覆盖 `PAYPALISHIRING/3 -> PAHNAPLSIIGYIR`、两行和一行退化情况。
- [ ] 确认 `main.py` 大小为 0。

### 任务 3：创建 0007 整数反转目录

**文件：**

- 创建 `problems/leetcode/0007_reverse_integer/problem.md`
- 创建 `problems/leetcode/0007_reverse_integer/notes.md`
- 创建空文件 `problems/leetcode/0007_reverse_integer/main.py`
- 创建 `tests/01.in`、`tests/01.out`、`tests/02.in`、`tests/02.out`、`tests/03.in`、`tests/03.out`

- [ ] 在题面中写明 32 位有符号输入、溢出输出 `0` 的规则。
- [ ] 测试覆盖正数末尾零、负数和反转溢出。
- [ ] 确认 `main.py` 大小为 0。

### 任务 4：创建 0008 字符串转换整数目录

**文件：**

- 创建 `problems/leetcode/0008_string_to_integer_atoi/problem.md`
- 创建 `problems/leetcode/0008_string_to_integer_atoi/notes.md`
- 创建空文件 `problems/leetcode/0008_string_to_integer_atoi/main.py`
- 创建 `tests/01.in`、`tests/01.out`、`tests/02.in`、`tests/02.out`、`tests/03.in`、`tests/03.out`、`tests/04.in`、`tests/04.out`

- [ ] 明确输入按整行读取，保留前导空格，空行代表空字符串。
- [ ] 明确符号、遇到非数字停止和 32 位上下界截断规则。
- [ ] 测试覆盖前导空格/符号、非数字终止、正负溢出和空行。
- [ ] 确认 `main.py` 大小为 0。

### 任务 5：创建 0009 回文数目录

**文件：**

- 创建 `problems/leetcode/0009_palindrome_number/problem.md`
- 创建 `problems/leetcode/0009_palindrome_number/notes.md`
- 创建空文件 `problems/leetcode/0009_palindrome_number/main.py`
- 创建 `tests/01.in`、`tests/01.out`、`tests/02.in`、`tests/02.out`、`tests/03.in`、`tests/03.out`

- [ ] 明确整数输入及 `true`/`false` 输出格式。
- [ ] 测试覆盖普通回文、负数和末尾为零的非零整数。
- [ ] 确认 `main.py` 大小为 0。

### 任务 6：创建 0010 正则表达式匹配目录

**文件：**

- 创建 `problems/leetcode/0010_regular_expression_matching/problem.md`
- 创建 `problems/leetcode/0010_regular_expression_matching/notes.md`
- 创建空文件 `problems/leetcode/0010_regular_expression_matching/main.py`
- 创建 `tests/01.in`、`tests/01.out`、`tests/02.in`、`tests/02.out`、`tests/03.in`、`tests/03.out`

- [ ] 明确两行输入、整串匹配、`.` 与 `*` 的语义及模式约束。
- [ ] 测试覆盖直接不匹配、`*` 多次匹配和组合模式。
- [ ] 确认 `main.py` 大小为 0。

### 任务 7：执行批量结构验证

**文件：** 不新增仓库代码；使用临时只读验证命令。

- [ ] 检查五个目录都包含 `problem.md`、`notes.md`、`main.py` 和 `tests/`。
- [ ] 检查每个 `main.py` 为 0 字节。
- [ ] 检查每个 `.in` 都有同名 `.out`，并确认每题至少三组。
- [ ] 比较 0005 基线哈希，确认其文件未被改动。
- [ ] 运行 `python -m unittest discover -s tests -v`，确认仓库工具测试不回归。
- [ ] 对新增空白目录运行 `python tools/run_tests.py <目录>` 仅记录其因空 `main.py` 产生的预期结果，不将其宣称为题解通过。

**完成标准：** 目录结构和测试夹具全部满足设计规格；0005 与仓库级工具无变化；没有把空白练习误报为 AC。

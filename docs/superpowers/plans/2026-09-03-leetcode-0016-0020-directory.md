# LeetCode 0016–0020 目录实现计划

> **面向 AI 代理的工作者：** 本计划用于当前会话内联执行。新增题目目录后逐题核验结构和测试契约，不实现学习者的解答。

**目标：** 按仓库 ACM 约定新增 LeetCode 0016–0020 五个可练习目录。

**方案：** 使用 `tools/new_problem.py` 创建骨架；先填写本地测试输入输出，再补充题面与笔记模板；清空 `main.py` 作为练习入口；最后运行结构检查和逐题测试命令。

**技术栈：** Python 标准库、UTF-8 Markdown、现有 `tools/run_tests.py`。

---

### 任务 1：创建五个统一目录骨架

**文件：**

- 创建 `problems/leetcode/0016_3sum_closest/`
- 创建 `problems/leetcode/0017_letter_combinations_of_a_phone_number/`
- 创建 `problems/leetcode/0018_4sum/`
- 创建 `problems/leetcode/0019_remove_nth_node_from_end_of_list/`
- 创建 `problems/leetcode/0020_valid_parentheses/`

- [ ] 使用 `python tools/new_problem.py leetcode <number> <slug>` 创建目录。
- [ ] 确认每个目录包含 `problem.md`、`main.py`、`notes.md` 和 `tests/01.in`、`tests/01.out`。

### 任务 2：先建立输入输出测试契约

**文件：** 五个目录下的 `tests/*.in` 与 `tests/*.out`。

- [ ] 为 0016 准备普通样例、重复/负数样例和三元素边界样例。
- [ ] 为 0017 准备两位、单位和空输入样例。
- [ ] 为 0018 准备典型样例、重复元素、无解和多解样例。
- [ ] 为 0019 准备删除中间节点、头节点、单节点和尾节点样例。
- [ ] 为 0020 准备有效嵌套、无效交叉、孤立右括号和空输入样例。
- [ ] 运行空骨架，确认测试不是空文件且预期会因未实现而不通过。

### 任务 3：填写题面与练习笔记

**文件：** 每个目录的 `problem.md`、`notes.md`。

- [ ] 写入来源链接、难度、标签、题意摘要、完整本地 ACM 输入输出协议、约束和示例。
- [ ] 在 `notes.md` 中保留核心观察、复杂度和边界记录位置，不写完整解答。
- [ ] 明确排序、去重、空输入和输出顺序等容易产生歧义的规则。

### 任务 4：保留空解题入口并执行最终验证

**文件：** 每个目录的 `main.py`。

- [ ] 清除生成器中的占位解析代码，保留空文件作为学习入口。
- [ ] 检查五个目录路径、文件清单、测试配对和 UTF-8 可读性。
- [ ] 运行 `python tools/run_tests.py <problem-directory>`，记录空入口的预期未通过状态，不宣称题目 AC。
- [ ] 运行仓库工具测试 `python -m unittest discover -s tests -v`。
- [ ] 检查最终 diff，确认没有改动已有题目或工具。

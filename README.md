# Python ACM 刷题仓库

使用 Python 完整程序练习 LeetCode Hot 100、其他 LeetCode 题目及公司机考题。每道题自行处理标准输入和标准输出，采用本地定义的 ACM 协议。

这是个人学习记录，包含已实现代码、尚未完成的尝试和预留练习。当前代码不保证全部通过；请先查看题目状态及 [本地验证记录](docs/local_validation.md)。本地测试通过不等同于官方 AC，也不代表已完成全面正确性或复杂度审查。

## 环境

- Python 3.10 或以上版本。
- 仅使用 Python 标准库，无需安装第三方依赖。
- Windows、Linux 或 macOS 均可运行；以下命令从仓库根目录执行。
- 文本文件使用 UTF-8，Git 按 `.gitattributes` 统一换行符。

## 目录

| 路径 | 内容 |
| --- | --- |
| [problems/hot100/](problems/hot100/) | Hot 100，使用内部顺序与原题号命名 |
| [problems/leetcode/](problems/leetcode/) | 历史 LeetCode 练习，保留原目录 |
| [sets/](sets/) | 题单、进度、复习与模拟考试索引 |
| [templates/](templates/) | 单组、多组、EOF、矩阵及图的输入模板 |
| [notes/](notes/) | 输入输出、错题和算法专题笔记 |
| [tools/](tools/) | 新建题目、单题测试和结构检查工具 |
| [tests/](tests/) | 仓库工具、模板和示例的单元测试 |
| [docs/](docs/) | 本地验证记录、来源说明、设计和实施记录 |
| [AGENTS.md](AGENTS.md) | 统一 AI 协作及分层指导规则 |

Hot 100 范围、内部顺序和进度统一维护在 [sets/leetcode_hot100.md](sets/leetcode_hot100.md)。历史目录与 Hot 100 同题目录可能同时存在，代表不同练习记录，不需要删除或迁移。

## 单题结构与练习

```text
problems/hot100/01_0001_two_sum/
├── problem.md
├── main.py
├── notes.md
└── tests/
    ├── 01.in
    ├── 01.out
    └── …（至少 8 组完整用例）
```

先阅读 `problem.md` 的来源、难度、标签、输入输出协议与约束，再编写 `main.py`。所有解答以 `solve()` 和 `if __name__ == "__main__"` 为入口。空文件或骨架属于未实现练习；保留尝试供后续学习。

运行单题测试：

```text
python tools/run_tests.py problems/hot100/01_0001_two_sum
python tools/run_tests.py problems/hot100/01_0001_two_sum --timeout 5
```

工具会报告 `PASS`、`WRONG_ANSWER`、`RUNTIME_ERROR` 或 `TIMEOUT`。输出严格比较，只统一换行符并忽略末尾换行；多解题必须在本地协议中约定唯一输出顺序或构造方式。

## 新建练习

按本地题单顺序创建 Hot 100 草稿，并自动添加题单链接：

```text
python tools/new_problem.py hot100 11 76 minimum_window_substring
```

依次传入内部顺序、真实 LeetCode 题号和下划线 slug；工具会核对本地题单并拒绝覆盖已有目录。

明确来源为其他 LeetCode 题目或公司题目时：

```text
python tools/new_problem.py leetcode 49 group_anagrams
python tools/new_problem.py company meituan 2026-08-18 1 problem_name
```

新建工具只生成草稿，`01.in/01.out` 是空占位文件，不是有效测试。开始练习前须填写难度、标签、输入输出和约束，替换占位内容并补齐至少 8 组有效测试；草稿尚未补齐时结构检查会失败。

## 仓库验证

```text
python -m unittest discover -s tests -v
python tools/check_repository.py
```

GitHub Actions 会在 Python 3.10 和 3.13 上运行上述检查。CI 验证工具、模板、示例、文档链接及题目结构；每道练习的算法状态单独记录，以便保留未完成尝试。

改动解答后运行该题全部用例，更新题目状态、验证记录和 Hot 100 题单。改变本地协议时同步检查所有期望输出；不要仅为了让测试通过而修改正确的期望答案。

## 上传范围与来源

代码、题目摘要、笔记、题单、工具及全部 `.in/.out` 文件应提交。Python 缓存、虚拟环境、编辑器个人设置、环境变量文件和临时文件由 `.gitignore` 排除。

题面使用个人摘要和本地输入输出协议，原题保留链接；详见 [来源与使用说明](docs/sources.md)。当前未选择开源许可证，不自动授予原创内容的再分发许可；第三方内容的权利仍属于其权利人。

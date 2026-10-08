# Python ACM 刷题仓库实现计划

> **面向 AI 代理的工作者：** 必需子技能：使用 `executing-plans` 在当前会话中逐任务实施；如果用户明确要求代理委派，才改用 `subagent-driven-development`。每完成一个任务都运行该任务的验证命令并更新复选框。

**目标：** 建立一个以 Python 完整 ACM 输入输出程序为核心、带本地测试工具和 Codex AI 教练规则的个人刷题仓库。

**架构：** 题目代码按来源唯一存储，题单与专题只链接到题目目录。本地 Python 工具负责创建题目和精确运行样例；根目录 `AGENTS.md` 负责约束 Codex 的判题、提示和代码修改行为。所有实现仅依赖 Python 标准库。

**技术栈：** Python 3.10+（当前环境为 Python 3.13.5）、`unittest`、`pathlib`、`argparse`、`subprocess`、Markdown、Codex `AGENTS.md`

---

## 文件结构与职责

### 根目录

- 创建：`AGENTS.md`——Codex 在本仓库中的项目级工作规则。
- 创建：`README.md`——项目目标、目录说明和常用命令。
- 创建：`.gitignore`——忽略 Python 缓存、虚拟环境、编辑器文件和临时输出。

### 工具与测试

- 创建：`tools/__init__.py`——使工具可以被标准库测试直接导入。
- 创建：`tools/run_tests.py`——发现并执行单题 `.in`/`.out` 测试。
- 创建：`tools/new_problem.py`——创建统一的 LeetCode 或公司机考题目录。
- 创建：`tests/__init__.py`——使按模块名称运行的测试在各环境中行为一致。
- 创建：`tests/test_run_tests.py`——覆盖通过、答案错误、运行错误、超时和配置错误。
- 创建：`tests/test_new_problem.py`——覆盖两类目录创建、参数校验和拒绝覆盖。
- 创建：`tests/test_templates.py`——对五种模板做语法与代表性输入烟雾测试。
- 创建：`tests/test_example_problem.py`——验证两数之和示例目录能被测试工具正确执行。

### ACM 模板

- 创建：`templates/single_case.py`——单组输入模板。
- 创建：`templates/multiple_cases.py`——首行测试组数模板。
- 创建：`templates/until_eof.py`——读取到 EOF 模板。
- 创建：`templates/matrix.py`——矩阵输入模板。
- 创建：`templates/graph.py`——图的边集输入模板。

### 首道示例题

- 创建：`problems/leetcode/0001_two_sum/problem.md`——来源、约束和 ACM 输入协议。
- 创建：`problems/leetcode/0001_two_sum/main.py`——哈希表解法的完整 ACM 程序。
- 创建：`problems/leetcode/0001_two_sum/notes.md`——复杂度和边界记录。
- 创建：`problems/leetcode/0001_two_sum/tests/01.in`、`01.out`——普通样例。
- 创建：`problems/leetcode/0001_two_sum/tests/02.in`、`02.out`——重复数字样例。
- 创建：`problems/leetcode/0001_two_sum/tests/03.in`、`03.out`——负数样例。

### 题单与笔记

- 创建：`sets/leetcode_hot100.md`——Hot 100 来源和进度索引。
- 创建：`sets/huawei_od.md`——华为机考题源入口和后续索引格式。
- 创建：`sets/company_interviews.md`——公司、日期、场次索引格式。
- 创建：`sets/mock_exams/README.md`——限时模拟场次约定。
- 创建：`notes/input_output.md`——Python ACM 常用输入输出说明。
- 创建：`notes/mistakes.md`——错题复盘索引。
- 创建：`notes/topics/README.md`——算法专题索引。

## 实施说明

当前目录不是 Git 仓库，因而无法创建专用 worktree，也不安排 commit 步骤。实施期间只在当前目录中写入上述文件；是否执行 `git init` 留给用户单独决定。

---

### 任务 1：建立根目录规则和项目入口

**文件：**

- 创建：`AGENTS.md`
- 创建：`README.md`
- 创建：`.gitignore`
- 创建：`tools/__init__.py`
- 创建：`tests/__init__.py`

- [ ] **步骤 1：创建 Codex 项目级规则**

在 `AGENTS.md` 中写入以下完整规则边界：

```markdown
# Python ACM Practice Repository

## Scope

- Use Python for all solutions.
- Write complete ACM-style programs that read stdin and write stdout.
- Keep `solve()` plus the `if __name__ == "__main__"` entry point.
- Prefer the Python standard library unless the user explicitly approves a dependency.

## Judge workflow

- Read `problem.md`, `main.py`, and all local cases before judging.
- Run local tests before reporting a result.
- Check correctness, input parsing, output formatting, time complexity, space complexity, and edge cases.
- Try to produce a minimal counterexample for every suspected bug.
- Report only local evidence. Never call a local pass an official AC.
- Use one of: local tests pass, counterexample found, runtime error, timeout risk, format error, or insufficient information.

## Coaching workflow

- Preserve the learner's attempt and reasoning.
- Start with a directional hint, then a stronger hint, then pseudocode.
- Give a complete solution only when explicitly requested.
- Do not edit a learner's `main.py` unless explicitly asked to fix or implement it.
- When fixing a bug, add a regression case that fails before the fix.

## Repository conventions

- LeetCode path: `problems/leetcode/<four-digit-id>_<slug>/`.
- Company path: `problems/company/<company>/<session>/<qNN>_<slug>/`.
- A problem directory contains `problem.md`, `main.py`, `notes.md`, and `tests/`.
- Keep source URLs and personal summaries; do not bulk-copy unlicensed statements or solutions.
- Run `python -m unittest discover -s tests -v` after changing repository tools.
```

- [ ] **步骤 2：创建 README 使用入口**

`README.md` 必须说明：

```markdown
# Python ACM 刷题仓库

本仓库使用 Python 完整程序练习 LeetCode 与大厂机考题。

## 常用命令

python tools/run_tests.py problems/leetcode/0001_two_sum
python tools/new_problem.py leetcode 49 group_anagrams
python tools/new_problem.py company meituan 2026-08-18 1 problem_name
python -m unittest discover -s tests -v
```

同时链接 `sets/`、`notes/`、`templates/` 和设计规格，不复制设计文档的大段内容。

- [ ] **步骤 3：创建忽略规则和工具包入口**

`.gitignore` 至少包含：

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.idea/
.vscode/
.pytest_cache/
.coverage
htmlcov/
*.tmp
```

`tools/__init__.py` 和 `tests/__init__.py` 只保留包说明，不执行副作用代码。

- [ ] **步骤 4：核对根目录文件内容**

运行：

```powershell
Get-Content -Raw AGENTS.md
Get-Content -Raw README.md
Get-Content -Raw .gitignore
```

预期：三个文件均可读取；`AGENTS.md` 同时包含 judge、coaching、ACM 和 test 规则。

---

### 任务 2：以 TDD 实现本地测试运行器

**文件：**

- 创建：`tests/test_run_tests.py`
- 创建：`tools/run_tests.py`

- [ ] **步骤 1：编写失败测试**

`tests/test_run_tests.py` 使用 `tempfile.TemporaryDirectory` 创建临时题目目录，并覆盖以下接口：

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.run_tests import ConfigError, discover_cases, run_problem


class RunTestsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.problem = Path(self.temp_dir.name)
        (self.problem / "tests").mkdir()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_program(self, source: str) -> None:
        (self.problem / "main.py").write_text(source, encoding="utf-8")

    def write_case(self, name: str, stdin: str, expected: str | None = None) -> None:
        (self.problem / "tests" / f"{name}.in").write_text(stdin, encoding="utf-8")
        if expected is not None:
            (self.problem / "tests" / f"{name}.out").write_text(expected, encoding="utf-8")

    def test_passes_and_ignores_only_trailing_newlines(self) -> None:
        self.write_program("print(input())\n")
        self.write_case("01", "hello\n", "hello\n\n")
        summary = run_problem(self.problem, timeout=1.0)
        self.assertEqual([result.status for result in summary.results], ["PASS"])

    def test_reports_wrong_answer_without_ignoring_spaces(self) -> None:
        self.write_program("print('hello ')\n")
        self.write_case("01", "", "hello\n")
        summary = run_problem(self.problem, timeout=1.0)
        self.assertEqual(summary.results[0].status, "WRONG_ANSWER")

    def test_reports_runtime_error(self) -> None:
        self.write_program("raise RuntimeError('boom')\n")
        self.write_case("01", "", "ignored\n")
        summary = run_problem(self.problem, timeout=1.0)
        self.assertEqual(summary.results[0].status, "RUNTIME_ERROR")

    def test_reports_timeout(self) -> None:
        self.write_program("while True:\n    pass\n")
        self.write_case("01", "", "")
        summary = run_problem(self.problem, timeout=0.1)
        self.assertEqual(summary.results[0].status, "TIMEOUT")

    def test_missing_output_is_a_configuration_error(self) -> None:
        self.write_program("print('x')\n")
        self.write_case("01", "")
        with self.assertRaises(ConfigError):
            discover_cases(self.problem)
```

- [ ] **步骤 2：运行测试并确认失败**

运行：

```text
python -m unittest tests.test_run_tests -v
```

预期：失败，原因是 `tools.run_tests` 尚不存在。

- [ ] **步骤 3：实现测试发现、执行和输出归一化**

`tools/run_tests.py` 定义以下稳定接口：

```python
@dataclass(frozen=True)
class TestCase:
    name: str
    input_path: Path
    output_path: Path


@dataclass(frozen=True)
class CaseResult:
    name: str
    status: str
    expected: str
    actual: str
    stderr: str


@dataclass(frozen=True)
class RunSummary:
    results: tuple[CaseResult, ...]

    @property
    def passed(self) -> bool:
        return bool(self.results) and all(result.status == "PASS" for result in self.results)


class ConfigError(ValueError):
    pass
```

实现规则：

```python
def normalize_output(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")


def discover_cases(problem_dir: Path) -> tuple[TestCase, ...]:
    main_path = problem_dir / "main.py"
    tests_dir = problem_dir / "tests"
    if not main_path.is_file():
        raise ConfigError(f"missing solution: {main_path}")
    if not tests_dir.is_dir():
        raise ConfigError(f"missing tests directory: {tests_dir}")
    inputs = sorted(tests_dir.glob("*.in"))
    if not inputs:
        raise ConfigError(f"no .in cases found in: {tests_dir}")
    cases = []
    for input_path in inputs:
        output_path = input_path.with_suffix(".out")
        if not output_path.is_file():
            raise ConfigError(f"missing expected output: {output_path}")
        cases.append(TestCase(input_path.stem, input_path, output_path))
    return tuple(cases)
```

`run_problem(problem_dir, timeout)` 使用：

```python
subprocess.run(
    [sys.executable, str(problem_dir / "main.py")],
    input=case.input_path.read_bytes(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    timeout=timeout,
    check=False,
)
```

返回状态只使用 `PASS`、`WRONG_ANSWER`、`RUNTIME_ERROR` 和 `TIMEOUT`。CLI 接受题目路径和 `--timeout`，全部通过返回 0，测试失败返回 1，配置或参数错误返回 2。

- [ ] **步骤 4：运行测试并确认通过**

运行：

```text
python -m unittest tests.test_run_tests -v
```

预期：5 个测试全部通过。

- [ ] **步骤 5：检查 CLI 错误退出码**

运行：

```text
python tools/run_tests.py missing-problem
```

预期：打印缺失 `main.py` 或目录的配置错误，进程退出码为 2。

---

### 任务 3：以 TDD 实现题目目录生成器

**文件：**

- 创建：`tests/test_new_problem.py`
- 创建：`tools/new_problem.py`

- [ ] **步骤 1：编写失败测试**

`tests/test_new_problem.py` 覆盖：

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.new_problem import ProblemExistsError, create_company_problem, create_leetcode_problem


class NewProblemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_creates_leetcode_problem(self) -> None:
        target = create_leetcode_problem(self.root, 49, "group_anagrams")
        self.assertEqual(target.relative_to(self.root).as_posix(), "problems/leetcode/0049_group_anagrams")
        self.assertTrue((target / "problem.md").is_file())
        self.assertTrue((target / "main.py").is_file())
        self.assertTrue((target / "notes.md").is_file())
        self.assertTrue((target / "tests" / "01.in").is_file())
        self.assertTrue((target / "tests" / "01.out").is_file())

    def test_creates_company_problem(self) -> None:
        target = create_company_problem(self.root, "meituan", "2026-08-18", 1, "problem_name")
        self.assertEqual(
            target.relative_to(self.root).as_posix(),
            "problems/company/meituan/2026-08-18/q01_problem_name",
        )

    def test_rejects_existing_target(self) -> None:
        create_leetcode_problem(self.root, 1, "two_sum")
        with self.assertRaises(ProblemExistsError):
            create_leetcode_problem(self.root, 1, "two_sum")

    def test_rejects_unsafe_slug(self) -> None:
        with self.assertRaises(ValueError):
            create_leetcode_problem(self.root, 1, "../escape")
```

- [ ] **步骤 2：运行测试并确认失败**

运行：

```text
python -m unittest tests.test_new_problem -v
```

预期：失败，原因是 `tools.new_problem` 尚不存在。

- [ ] **步骤 3：实现目录验证和文件生成**

`tools/new_problem.py` 提供：

```python
SAFE_NAME = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
SAFE_SESSION = re.compile(r"^(?:\d{4}-\d{2}-\d{2}|[a-z0-9]+(?:_[a-z0-9]+)*)$")


class ProblemExistsError(FileExistsError):
    pass


def require_name(value: str, label: str) -> str:
    if not SAFE_NAME.fullmatch(value):
        raise ValueError(f"invalid {label}: {value!r}")
    return value
```

公开函数签名：

```python
def create_leetcode_problem(root: Path, number: int, slug: str) -> Path:
    if number <= 0:
        raise ValueError("LeetCode number must be positive")
    safe_slug = require_name(slug, "slug")
    target = root / "problems" / "leetcode" / f"{number:04d}_{safe_slug}"
    return create_problem_files(target, title=f"LeetCode {number}")


def create_company_problem(
    root: Path,
    company: str,
    session: str,
    question_number: int,
    slug: str,
) -> Path:
    if question_number <= 0:
        raise ValueError("question number must be positive")
    safe_company = require_name(company, "company")
    safe_slug = require_name(slug, "slug")
    if not SAFE_SESSION.fullmatch(session):
        raise ValueError(f"invalid session: {session!r}")
    target = (
        root
        / "problems"
        / "company"
        / safe_company
        / session
        / f"q{question_number:02d}_{safe_slug}"
    )
    return create_problem_files(target, title=f"{safe_company} {session} Q{question_number}")
```

`create_problem_files(target, title)` 负责检查目标是否存在、创建目录和写入固定模板；发生异常时使用 `shutil.rmtree(target)` 只清理本次已经确认并创建的精确目标路径。两个公开函数都必须：

- 验证正整数题号和安全路径片段。
- 先确认目标不存在，再调用 `mkdir(parents=True)`。
- 写入 `problem.md`、`main.py`、`notes.md`、`tests/01.in`、`tests/01.out`。
- 生成的 `main.py` 含空的 `solve()` 和主入口，但不得含题解。
- 任一文件写入失败时清理本次刚创建的目标目录，避免半成品。

CLI 使用 `argparse` 子命令：

```text
new_problem.py leetcode NUMBER SLUG
new_problem.py company COMPANY SESSION QUESTION_NUMBER SLUG
```

- [ ] **步骤 4：运行测试并确认通过**

运行：

```text
python -m unittest tests.test_new_problem -v
```

预期：4 个测试全部通过。

- [ ] **步骤 5：验证 CLI 帮助和参数错误**

运行：

```text
python tools/new_problem.py --help
python tools/new_problem.py leetcode 0 invalid
```

预期：帮助命令退出码为 0；非法题号命令打印参数错误并以退出码 2 结束。

---

### 任务 4：以烟雾测试约束五种 ACM 模板

**文件：**

- 创建：`tests/test_templates.py`
- 创建：`templates/single_case.py`
- 创建：`templates/multiple_cases.py`
- 创建：`templates/until_eof.py`
- 创建：`templates/matrix.py`
- 创建：`templates/graph.py`

- [ ] **步骤 1：编写模板失败测试**

测试通过子进程运行每个模板，并验证代表性输入不会报错：

```python
TEMPLATE_CASES = {
    "single_case.py": ("3\n1 2 3\n", ""),
    "multiple_cases.py": ("2\n3\n1 2 3\n2\n4 5\n", ""),
    "until_eof.py": ("1 2\n3 4\n", ""),
    "matrix.py": ("2 3\n1 2 3\n4 5 6\n", ""),
    "graph.py": ("3 2\n1 2\n2 3\n", ""),
}
```

每个测试断言返回码为 0，标准错误为空。模板是输入骨架，不要求打印答案，因此预期标准输出为空。

- [ ] **步骤 2：运行测试并确认失败**

运行：

```text
python -m unittest tests.test_templates -v
```

预期：失败，原因是模板文件尚不存在。

- [ ] **步骤 3：实现五种模板**

每个文件遵循：

```python
import sys


def solve() -> None:
    _tokens = sys.stdin.buffer.read().split()


if __name__ == "__main__":
    solve()
```

具体解析结果分别为：

- `single_case.py`：读取首行规模和下一行整数数组。
- `multiple_cases.py`：读取测试组数，每组读取规模和整数数组。
- `until_eof.py`：将每个非空行解析为一组整数。
- `matrix.py`：读取行列数和指定行数的矩阵。
- `graph.py`：读取点数、边数并建立无向邻接表。

为避免未使用变量告警，模板可将解析结果赋给带下划线前缀的局部变量；不得输出示例答案。

- [ ] **步骤 4：运行模板测试并做语法检查**

运行：

```text
python -m unittest tests.test_templates -v
python -m compileall -q templates
```

预期：5 个模板烟雾测试通过，语法检查退出码为 0。

---

### 任务 5：以 TDD 添加首道完整 ACM 示例题

**文件：**

- 创建：`tests/test_example_problem.py`
- 创建：`problems/leetcode/0001_two_sum/problem.md`
- 创建：`problems/leetcode/0001_two_sum/main.py`
- 创建：`problems/leetcode/0001_two_sum/notes.md`
- 创建：`problems/leetcode/0001_two_sum/tests/01.in`
- 创建：`problems/leetcode/0001_two_sum/tests/01.out`
- 创建：`problems/leetcode/0001_two_sum/tests/02.in`
- 创建：`problems/leetcode/0001_two_sum/tests/02.out`
- 创建：`problems/leetcode/0001_two_sum/tests/03.in`
- 创建：`problems/leetcode/0001_two_sum/tests/03.out`

- [ ] **步骤 1：编写失败的集成测试**

```python
from pathlib import Path
import unittest

from tools.run_tests import run_problem


class ExampleProblemTest(unittest.TestCase):
    def test_two_sum_cases_pass(self) -> None:
        root = Path(__file__).resolve().parents[1]
        problem = root / "problems" / "leetcode" / "0001_two_sum"
        summary = run_problem(problem, timeout=1.0)
        self.assertTrue(summary.passed)
        self.assertEqual(len(summary.results), 3)
```

- [ ] **步骤 2：运行测试并确认失败**

运行：

```text
python -m unittest tests.test_example_problem -v
```

预期：失败，原因是示例题目录或 `main.py` 尚不存在。

- [ ] **步骤 3：创建题目文档和测试数据**

在 `problem.md` 中定义本地 ACM 协议：

```text
输入：第一行给出 n 和 target，第二行给出 n 个整数。
输出：按升序输出一组符合条件的零基下标，中间用一个空格分隔。
约束：保证恰好存在一组答案，同一元素不能重复使用。
```

测试数据：

```text
01.in:  4 9\n2 7 11 15\n     -> 01.out: 0 1\n
02.in:  2 6\n3 3\n           -> 02.out: 0 1\n
03.in:  3 -5\n-2 -3 7\n      -> 03.out: 0 1\n
```

- [ ] **步骤 4：实现最小哈希表解法**

`main.py`：

```python
import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, target = data[0], data[1]
    numbers = data[2 : 2 + n]
    seen: dict[int, int] = {}
    for index, value in enumerate(numbers):
        complement = target - value
        if complement in seen:
            print(seen[complement], index)
            return
        seen[value] = index


if __name__ == "__main__":
    solve()
```

`notes.md` 记录时间复杂度 `O(n)`、空间复杂度 `O(n)`，并说明必须先检查补数再写入当前值，才能正确处理两个相等数字。

- [ ] **步骤 5：运行示例题测试**

运行：

```text
python -m unittest tests.test_example_problem -v
python tools/run_tests.py problems/leetcode/0001_two_sum
```

预期：3 个题目用例全部显示 `PASS`，两个命令退出码均为 0。

---

### 任务 6：补齐题单、输入输出笔记和复盘入口

**文件：**

- 创建：`sets/leetcode_hot100.md`
- 创建：`sets/huawei_od.md`
- 创建：`sets/company_interviews.md`
- 创建：`sets/mock_exams/README.md`
- 创建：`notes/input_output.md`
- 创建：`notes/mistakes.md`
- 创建：`notes/topics/README.md`

- [ ] **步骤 1：创建 Hot 100 索引**

`sets/leetcode_hot100.md`：

- 链接 LeetCode 官方 Hot 100 题单。
- 按官方专题列出题目复选框、题号、中文题名、难度和本地目录链接。
- 只有 `0001_two_sum` 标记为已建立本地目录；其他题保持未完成。
- 不复制完整题面或第三方题解。

- [ ] **步骤 2：创建公司题目索引模板**

`sets/huawei_od.md` 至少保存牛客华为题库、已筛选 GitHub 参考仓库和本地路径格式；`sets/company_interviews.md` 使用以下表头：

```markdown
| 公司 | 日期/场次 | 题号 | 题目 | 标签 | 状态 | 本地目录 | 来源 |
|---|---|---:|---|---|---|---|---|
```

只收录已核对来源链接，不虚构题目名称、日期或难度。

- [ ] **步骤 3：创建模拟考试约定**

`sets/mock_exams/README.md` 定义：

- 一场模拟考试通过相对链接组合 2 至 5 道已有题目。
- 记录总时长、开始时间、结束时间和每题结果。
- 模拟期间不查看题解；Codex 只负责计时提醒和题意澄清。
- 结束后再让 Codex 运行测试并复盘。

- [ ] **步骤 4：创建输入输出和复盘笔记**

`notes/input_output.md` 必须包含可运行的 Python 示例：

```python
import sys

data = sys.stdin.buffer.read().split()
values = list(map(int, data))
```

并覆盖单行、多行、多测试组、EOF、矩阵和图输入的选择原则。

`notes/mistakes.md` 提供按日期记录“题目、症状、根因、最小反例、修复原则、复习日期”的表格。

`notes/topics/README.md` 提供哈希、双指针、滑动窗口、二分、栈、堆、回溯、贪心、动态规划、树和图等专题入口；在没有专题内容时不创建空目录。

- [ ] **步骤 5：检查 Markdown 链接和占位符**

运行一个只读 Python 检查脚本，遍历本地相对链接并确认目标存在，同时搜索被禁止的未完成标记：

```text
python -c "from pathlib import Path; import re; root=Path('.'); missing=[]; [missing.append((p,link)) for p in root.rglob('*.md') for link in re.findall(r'\[[^]]+\]\((?!https?://)([^)#]+)', p.read_text(encoding='utf-8')) if not (p.parent/link).resolve().exists()]; print(missing); raise SystemExit(bool(missing))"
```

预期：输出 `[]`，退出码为 0。题单中的未完成复选框 `- [ ]` 是有效进度标记，不作为设计占位符处理。

---

### 任务 7：执行完整验证和人工验收

**文件：**

- 修改：仅修改前述验证中发现问题的文件。

- [ ] **步骤 1：运行全部单元测试**

运行：

```text
python -m unittest discover -s tests -v
```

预期：测试运行器、题目生成器、模板和示例题的全部测试通过。

- [ ] **步骤 2：运行所有 Python 语法检查**

运行：

```text
python -m compileall -q tools templates problems tests
```

预期：退出码为 0，无语法错误。

- [ ] **步骤 3：验证真实 CLI 工作流**

在临时目录中运行题目创建器，避免污染正式题库：

```text
python -m unittest tests.test_new_problem -v
python tools/run_tests.py problems/leetcode/0001_two_sum --timeout 1
```

预期：生成器测试全部通过；两数之和 3 个用例全部 `PASS`。

- [ ] **步骤 4：人工检查 Codex 行为契约**

逐条核对 `AGENTS.md`：

- 是否规定完整 ACM 模式和 Python 标准库优先。
- 是否要求判题前运行测试。
- 是否禁止把本地通过表述为官方 AC。
- 是否要求提供最小反例和复杂度分析。
- 是否默认分层提示并保护使用者原始答案。
- 是否仅在明确要求时修改 `main.py`。

- [ ] **步骤 5：检查工作区最终文件列表**

运行：

```text
rg --files
```

预期：只包含设计文档、实现计划及本计划声明的项目文件，没有 `__pycache__`、临时生成题目或测试残留。

---

## 完成标准

只有当以下证据同时成立时才能宣称项目骨架完成：

1. `python -m unittest discover -s tests -v` 全部通过。
2. `python -m compileall -q tools templates problems tests` 退出码为 0。
3. `python tools/run_tests.py problems/leetcode/0001_two_sum --timeout 1` 报告 3 个 `PASS`。
4. 根目录 `AGENTS.md` 明确约束 Codex 判题和分层指导行为。
5. `new_problem.py` 对已存在目录拒绝覆盖。
6. 项目不包含 API Key、OpenAI API 调用或抓取平台题目的脚本。

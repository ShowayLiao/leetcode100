"""Create a consistently structured ACM problem directory."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import shutil
import sys


SAFE_NAME = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
DATE_SESSION = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ProblemExistsError(FileExistsError):
    """Raised when a generated problem would overwrite an existing path."""


def require_name(value: str, label: str) -> str:
    if not SAFE_NAME.fullmatch(value):
        raise ValueError(
            f"invalid {label}: {value!r}; use lowercase letters, digits, and underscores",
        )
    return value


def require_positive(value: int, label: str) -> int:
    if value <= 0:
        raise ValueError(f"{label} must be positive")
    return value


def require_session(value: str) -> str:
    if DATE_SESSION.fullmatch(value):
        try:
            date.fromisoformat(value)
        except ValueError as error:
            raise ValueError(f"invalid session date: {value!r}") from error
        return value
    return require_name(value, "session")


def _problem_markdown(title: str) -> str:
    return f"""# {title}

> 状态：草稿。开始解题前请补全来源、输入输出和数据范围。

## 来源

- 原题链接：
- Difficulty: 待填写
- Tags: 待填写

## 题目摘要

请使用自己的语言记录题意。

## 输入描述

开始解题前记录完整输入协议。

## 输出描述

开始解题前记录完整输出协议。

## 数据范围

开始解题前记录影响复杂度选择的数据范围。

## 样例说明

样例保存在 `tests/` 目录。生成的 01.in/01.out 是空占位文件，不是有效测试。
开始练习前，至少补齐 8 组有效的输入与期望输出，并补全上述元数据。
"""


MAIN_TEMPLATE = '''import sys


def solve() -> None:
    _data = sys.stdin.buffer.read().split()


if __name__ == "__main__":
    solve()
'''


NOTES_TEMPLATE = """# 解题笔记

## 思路

完成题目后记录关键观察和算法过程。

## 复杂度

- 时间复杂度：完成题目后记录。
- 空间复杂度：完成题目后记录。

## 错误与边界

记录最小反例、错误根因和修复原则。
"""


def create_problem_files(target: Path, title: str) -> Path:
    """Create one problem atomically enough to avoid a partial target directory."""

    target = Path(target)
    if target.exists():
        raise ProblemExistsError(f"problem already exists: {target}")

    try:
        target.mkdir(parents=True, exist_ok=False)
    except FileExistsError as error:
        raise ProblemExistsError(f"problem already exists: {target}") from error

    try:
        tests_dir = target / "tests"
        tests_dir.mkdir()
        (target / "problem.md").write_text(_problem_markdown(title), encoding="utf-8")
        (target / "main.py").write_text(MAIN_TEMPLATE, encoding="utf-8")
        (target / "notes.md").write_text(NOTES_TEMPLATE, encoding="utf-8")
        (tests_dir / "01.in").write_text("", encoding="utf-8")
        (tests_dir / "01.out").write_text("", encoding="utf-8")
    except Exception:
        shutil.rmtree(target)
        raise
    return target


def create_leetcode_problem(root: Path, number: int, slug: str) -> Path:
    safe_number = require_positive(number, "LeetCode number")
    safe_slug = require_name(slug, "slug")
    target = Path(root) / "problems" / "leetcode" / f"{safe_number:04d}_{safe_slug}"
    result = create_problem_files(target, title=f"LeetCode {safe_number}")
    problem = result / "problem.md"
    problem.write_text(problem.read_text(encoding="utf-8").replace(
        "- 原题链接：", f"- 原题链接：https://leetcode.cn/problems/{safe_slug.replace('_', '-')}/",
    ), encoding="utf-8")
    return result


def create_hot100_problem(root: Path, order: int, number: int, slug: str) -> Path:
    """Create a draft only when order, id and slug match the local index."""
    require_positive(order, "internal order")
    require_positive(number, "LeetCode number")
    require_name(slug, "slug")
    index = Path(root) / "sets" / "leetcode_hot100.md"
    if not index.is_file():
        raise ValueError("missing Hot 100 index: sets/leetcode_hot100.md")
    original = index.read_text(encoding="utf-8")
    entries = list(re.finditer(
        r"^- \[[ x]\] (\d+)\. .*?https://leetcode\.cn/problems/([^/]+)/.*$",
        original, re.MULTILINE,
    ))
    if order > len(entries):
        raise ValueError("internal order is outside the Hot 100 index")
    entry = entries[order - 1]
    if int(entry.group(1)) != number or entry.group(2).replace("-", "_") != slug:
        raise ValueError("order, number and slug must match the local Hot 100 index")
    hot100 = Path(root) / "problems" / "hot100"
    if any(hot100.glob(f"{order:02d}_*")) or any(hot100.glob(f"*_{number:04d}_*")):
        raise ProblemExistsError("Hot 100 order or problem already exists")
    target = hot100 / f"{order:02d}_{number:04d}_{slug}"
    result = create_problem_files(target, title=f"LeetCode Hot 100 {order:02d} - {number}")
    try:
        problem = result / "problem.md"
        problem.write_text(problem.read_text(encoding="utf-8").replace(
            "- 原题链接：", f"- 原题链接：https://leetcode.cn/problems/{entry.group(2)}/",
        ), encoding="utf-8")
        line = re.sub(r"\s*— 未建题\s*$", "", entry.group(0))
        link = f"[Hot100练习](../problems/hot100/{target.name}/)"
        updated = re.sub(r"\[Hot100练习\]\([^)]+\)", link, line) if "[Hot100练习]" in line else line + " — " + link
        index_text = original[:entry.start()] + updated + " · 草稿" + original[entry.end():]
        built_count = sum((path / "main.py").is_file() for path in hot100.iterdir() if path.is_dir())
        index_text = re.sub(r"已建题 \d+ / 100", f"已建题 {built_count} / 100", index_text)
        index.write_text(index_text, encoding="utf-8")
    except Exception:
        shutil.rmtree(result)
        raise
    return result


def create_company_problem(
    root: Path,
    company: str,
    session: str,
    question_number: int,
    slug: str,
) -> Path:
    safe_company = require_name(company, "company")
    safe_session = require_session(session)
    safe_question = require_positive(question_number, "question number")
    safe_slug = require_name(slug, "slug")
    target = (
        Path(root)
        / "problems"
        / "company"
        / safe_company
        / safe_session
        / f"q{safe_question:02d}_{safe_slug}"
    )
    return create_problem_files(
        target,
        title=f"{safe_company} {safe_session} Q{safe_question}",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create an ACM problem directory.")
    subparsers = parser.add_subparsers(dest="kind", required=True)

    leetcode = subparsers.add_parser("leetcode", help="create a LeetCode problem")
    leetcode.add_argument("number", type=int)
    leetcode.add_argument("slug")

    hot100 = subparsers.add_parser("hot100", help="create a Hot 100 draft and update its index")
    hot100.add_argument("order", type=int, help="internal position in sets/leetcode_hot100.md")
    hot100.add_argument("number", type=int)
    hot100.add_argument("slug")

    company = subparsers.add_parser("company", help="create a company exam problem")
    company.add_argument("company")
    company.add_argument("session", help="YYYY-MM-DD or a name such as od or undated")
    company.add_argument("question_number", type=int)
    company.add_argument("slug")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    try:
        if args.kind == "leetcode":
            target = create_leetcode_problem(root, args.number, args.slug)
        elif args.kind == "hot100":
            target = create_hot100_problem(root, args.order, args.number, args.slug)
        else:
            target = create_company_problem(
                root,
                args.company,
                args.session,
                args.question_number,
                args.slug,
            )
    except (ProblemExistsError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    print(target.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


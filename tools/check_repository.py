"""Check publishable learning material; unfinished solutions are allowed."""

from pathlib import Path
import re
import sys


def check_repository(root: Path) -> list[str]:
    errors = []
    for problem in sorted((root / "problems").rglob("problem.md")):
        directory = problem.parent
        label = directory.relative_to(root).as_posix()
        for name in ("main.py", "notes.md", "tests"):
            if not (directory / name).exists():
                errors.append(f"{label}: missing {name}")
        inputs = {p.stem for p in (directory / "tests").glob("*.in")}
        outputs = {p.stem for p in (directory / "tests").glob("*.out")}
        if inputs != outputs:
            errors.append(f"{label}: unpaired tests {sorted(inputs ^ outputs)}")
        if len(inputs & outputs) < 8:
            errors.append(f"{label}: requires at least 8 test pairs")
        text = problem.read_text(encoding="utf-8")
        metadata = {
            "source": r"https?://", "difficulty": r"Difficulty:|难度[：:]",
            "tags": r"Tags:|标签[：:]", "input": r"## .*?(?:[Ii]nput|输入)",
            "output": r"## .*?(?:[Oo]utput|输出)",
            "constraints": r"## .*?(?:Constraints|数据范围|约束)",
            "example": r"## .*?(?:Example|样例|示例|测试)",
        }
        missing = [key for key, pattern in metadata.items() if not re.search(pattern, text)]
        if missing:
            errors.append(f"{label}: missing metadata {missing}")
    for directory in (root / "problems").rglob("main.py"):
        if not (directory.parent / "problem.md").is_file():
            errors.append(f"{directory.relative_to(root)}: missing problem.md")
    for document in sorted(root.rglob("*.md")):
        if any(part in (".git", ".venv", "venv") for part in document.parts):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if path and not (document.parent / path).exists():
                errors.append(f"{document.relative_to(root)}: broken link {target}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check_repository(root)
    for error in errors:
        print(error)
    if errors:
        print(f"{len(errors)} repository issue(s)", file=sys.stderr)
        return 1
    print("Repository structure, metadata, links and test pairs checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

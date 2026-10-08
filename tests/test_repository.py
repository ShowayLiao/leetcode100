from pathlib import Path
import importlib.util
from tempfile import TemporaryDirectory
import unittest


class RepositoryCheckTest(unittest.TestCase):
    def test_checker_rejects_missing_pairs_and_metadata(self) -> None:
        self.assertIsNotNone(importlib.util.find_spec("tools.check_repository"))
        from tools.check_repository import check_repository

        with TemporaryDirectory() as temp:
            root = Path(temp)
            problem = root / "problems" / "leetcode" / "0001_two_sum"
            (problem / "tests").mkdir(parents=True)
            (problem / "main.py").write_text("", encoding="utf-8")
            (problem / "notes.md").write_text("Notes", encoding="utf-8")
            (problem / "problem.md").write_text("Draft", encoding="utf-8")
            (problem / "tests" / "01.in").write_text("", encoding="utf-8")
            errors = check_repository(root)
            self.assertTrue(any("8" in e for e in errors))
            self.assertTrue(any("01" in e for e in errors))
            self.assertTrue(any("metadata" in e for e in errors))

    def test_checker_accepts_complete_learning_directory(self) -> None:
        self.assertIsNotNone(importlib.util.find_spec("tools.check_repository"))
        from tools.check_repository import check_repository

        with TemporaryDirectory() as temp:
            root = Path(temp)
            problem = root / "problems" / "leetcode" / "0001_two_sum"
            (problem / "tests").mkdir(parents=True)
            (problem / "main.py").write_text("", encoding="utf-8")
            (problem / "notes.md").write_text("Notes", encoding="utf-8")
            (problem / "problem.md").write_text(
                "https://leetcode.cn/problems/two-sum/\nDifficulty: Easy\nTags: Hash\n"
                "## Input\n## Output\n## Constraints\n## Example\n", encoding="utf-8",
            )
            for i in range(1, 9):
                for suffix in ("in", "out"):
                    (problem / "tests" / f"{i:02d}.{suffix}").write_text("\n", encoding="utf-8")
            self.assertEqual(check_repository(root), [])

    def test_actual_repository_layout(self) -> None:
        self.assertIsNotNone(importlib.util.find_spec("tools.check_repository"))
        from tools.check_repository import check_repository

        self.assertEqual(check_repository(Path(__file__).resolve().parents[1]), [])


if __name__ == "__main__":
    unittest.main()

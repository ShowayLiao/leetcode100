from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.new_problem import (
    ProblemExistsError,
    create_company_problem,
    create_leetcode_problem,
)


class NewProblemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_hot100_uses_internal_order_and_updates_index(self) -> None:
        from tools import new_problem

        self.assertTrue(hasattr(new_problem, "create_hot100_problem"))
        index = self.root / "sets" / "leetcode_hot100.md"
        index.parent.mkdir()
        index.write_text(
            "- 当前本地进度：0 / 100 道本地用例通过；已建题 0 / 100。\n"
            "- [ ] 1. [Two Sum](https://leetcode.cn/problems/two-sum/)\n"
            "- [ ] 49. [Group Anagrams](https://leetcode.cn/problems/group-anagrams/) — 未建题\n",
            encoding="utf-8",
        )
        target = new_problem.create_hot100_problem(self.root, 2, 49, "group_anagrams")
        self.assertEqual(target.name, "02_0049_group_anagrams")
        self.assertIn("../problems/hot100/02_0049_group_anagrams/", index.read_text(encoding="utf-8"))
        self.assertNotIn("未建题", index.read_text(encoding="utf-8"))
        self.assertIn("已建题 1 / 100", index.read_text(encoding="utf-8"))
        self.assertIn("https://leetcode.cn/problems/group-anagrams/", (target / "problem.md").read_text(encoding="utf-8"))
        self.assertIn("Difficulty:", (target / "problem.md").read_text(encoding="utf-8"))
        self.assertIn("Tags:", (target / "problem.md").read_text(encoding="utf-8"))
        before = index.read_bytes()
        with self.assertRaises(ValueError):
            new_problem.create_hot100_problem(self.root, 1, 49, "group_anagrams")
        self.assertEqual(before, index.read_bytes())
        with self.assertRaises(ProblemExistsError):
            new_problem.create_hot100_problem(self.root, 2, 49, "group_anagrams")
        self.assertEqual(before, index.read_bytes())

    def test_generated_draft_has_metadata_and_test_warning(self) -> None:
        target = create_leetcode_problem(self.root, 49, "group_anagrams")
        text = (target / "problem.md").read_text(encoding="utf-8")
        self.assertIn("Difficulty:", text)
        self.assertIn("Tags:", text)
        self.assertIn("8", text)

    def test_creates_leetcode_problem(self) -> None:
        target = create_leetcode_problem(self.root, 49, "group_anagrams")

        self.assertEqual(
            target.relative_to(self.root).as_posix(),
            "problems/leetcode/0049_group_anagrams",
        )
        self.assertTrue((target / "problem.md").is_file())
        self.assertTrue((target / "main.py").is_file())
        self.assertTrue((target / "notes.md").is_file())
        self.assertTrue((target / "tests" / "01.in").is_file())
        self.assertTrue((target / "tests" / "01.out").is_file())
        self.assertIn("def solve() -> None:", (target / "main.py").read_text(encoding="utf-8"))

    def test_creates_company_problem(self) -> None:
        target = create_company_problem(
            self.root,
            "meituan",
            "2026-08-18",
            1,
            "problem_name",
        )

        self.assertEqual(
            target.relative_to(self.root).as_posix(),
            "problems/company/meituan/2026-08-18/q01_problem_name",
        )

    def test_rejects_existing_target(self) -> None:
        target = create_leetcode_problem(self.root, 1, "two_sum")
        original = (target / "main.py").read_text(encoding="utf-8")

        with self.assertRaises(ProblemExistsError):
            create_leetcode_problem(self.root, 1, "two_sum")

        self.assertEqual((target / "main.py").read_text(encoding="utf-8"), original)

    def test_rejects_unsafe_slug(self) -> None:
        with self.assertRaises(ValueError):
            create_leetcode_problem(self.root, 1, "../escape")

    def test_rejects_invalid_company_session(self) -> None:
        with self.assertRaises(ValueError):
            create_company_problem(self.root, "meituan", "../../escape", 1, "problem")


if __name__ == "__main__":
    unittest.main()


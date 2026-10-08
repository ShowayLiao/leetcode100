from pathlib import Path
import unittest

from tools.run_tests import run_problem


class ExampleProblemTest(unittest.TestCase):
    def test_two_sum_cases_pass(self) -> None:
        root = Path(__file__).resolve().parents[1]
        problem = root / "problems" / "leetcode" / "0001_two_sum"

        summary = run_problem(problem, timeout=1.0)

        self.assertTrue(summary.passed)
        self.assertGreaterEqual(len(summary.results), 8)


if __name__ == "__main__":
    unittest.main()


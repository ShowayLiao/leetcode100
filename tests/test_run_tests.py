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
            (self.problem / "tests" / f"{name}.out").write_text(
                expected,
                encoding="utf-8",
            )

    def test_passes_and_ignores_only_trailing_newlines(self) -> None:
        self.write_program("print(input())\n")
        self.write_case("01", "hello\n", "hello\n\n")

        summary = run_problem(self.problem, timeout=1.0)

        self.assertTrue(summary.passed)
        self.assertEqual([result.status for result in summary.results], ["PASS"])

    def test_reports_wrong_answer_without_ignoring_spaces(self) -> None:
        self.write_program("print('hello ')\n")
        self.write_case("01", "", "hello\n")

        summary = run_problem(self.problem, timeout=1.0)

        self.assertFalse(summary.passed)
        self.assertEqual(summary.results[0].status, "WRONG_ANSWER")

    def test_reports_runtime_error(self) -> None:
        self.write_program("raise RuntimeError('boom')\n")
        self.write_case("01", "", "ignored\n")

        summary = run_problem(self.problem, timeout=1.0)

        self.assertEqual(summary.results[0].status, "RUNTIME_ERROR")
        self.assertIn("RuntimeError: boom", summary.results[0].stderr)

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

    def test_missing_tests_are_a_configuration_error(self) -> None:
        self.write_program("print('x')\n")

        with self.assertRaises(ConfigError):
            discover_cases(self.problem)

    def test_orphan_output_is_a_configuration_error(self) -> None:
        self.write_program("print('x')\n")
        self.write_case("01", "", "x\n")
        (self.problem / "tests" / "02.out").write_text("x\n", encoding="utf-8")

        with self.assertRaises(ConfigError):
            discover_cases(self.problem)


if __name__ == "__main__":
    unittest.main()


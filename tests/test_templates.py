from pathlib import Path
import subprocess
import sys
import unittest


class TemplateSmokeTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1]

    def run_template(self, filename: str, stdin: str) -> None:
        completed = subprocess.run(
            [sys.executable, str(self.root / "templates" / filename)],
            input=stdin,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=1.0,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout, "")
        self.assertEqual(completed.stderr, "")

    def test_single_case_template(self) -> None:
        self.run_template("single_case.py", "3\n1 2 3\n")

    def test_multiple_cases_template(self) -> None:
        self.run_template("multiple_cases.py", "2\n3\n1 2 3\n2\n4 5\n")

    def test_until_eof_template(self) -> None:
        self.run_template("until_eof.py", "1 2\n3 4\n")

    def test_matrix_template(self) -> None:
        self.run_template("matrix.py", "2 3\n1 2 3\n4 5 6\n")

    def test_graph_template(self) -> None:
        self.run_template("graph.py", "3 2\n1 2\n2 3\n")


if __name__ == "__main__":
    unittest.main()


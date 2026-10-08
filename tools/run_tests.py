"""Run ACM-style solutions against matching .in/.out files."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys


PASS = "PASS"
WRONG_ANSWER = "WRONG_ANSWER"
RUNTIME_ERROR = "RUNTIME_ERROR"
TIMEOUT = "TIMEOUT"


class ConfigError(ValueError):
    """Raised when a problem directory cannot be tested as configured."""


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
        return bool(self.results) and all(result.status == PASS for result in self.results)


def normalize_output(text: str) -> str:
    """Normalize line endings and ignore only newlines at end of output."""

    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")


def discover_cases(problem_dir: Path) -> tuple[TestCase, ...]:
    """Return sorted test pairs or raise ConfigError for an invalid layout."""

    problem_dir = Path(problem_dir)
    main_path = problem_dir / "main.py"
    tests_dir = problem_dir / "tests"
    if not main_path.is_file():
        raise ConfigError(f"missing solution: {main_path}")
    if not tests_dir.is_dir():
        raise ConfigError(f"missing tests directory: {tests_dir}")

    input_paths = sorted(tests_dir.glob("*.in"))
    if not input_paths:
        raise ConfigError(f"no .in cases found in: {tests_dir}")

    input_names = {path.stem for path in input_paths}
    orphan_outputs = sorted(path.name for path in tests_dir.glob("*.out") if path.stem not in input_names)
    if orphan_outputs:
        raise ConfigError(f"expected outputs without input: {', '.join(orphan_outputs)}")

    cases: list[TestCase] = []
    for input_path in input_paths:
        output_path = input_path.with_suffix(".out")
        if not output_path.is_file():
            raise ConfigError(f"missing expected output: {output_path}")
        cases.append(TestCase(input_path.stem, input_path, output_path))
    return tuple(cases)


def _decode(value: bytes | str | None) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return value.decode("utf-8", errors="replace")


def run_case(problem_dir: Path, case: TestCase, timeout: float) -> CaseResult:
    """Run one test case and classify the observable result."""

    expected = normalize_output(case.output_path.read_text(encoding="utf-8"))
    try:
        completed = subprocess.run(
            [sys.executable, str(problem_dir / "main.py")],
            cwd=problem_dir,
            input=case.input_path.read_bytes(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        return CaseResult(
            name=case.name,
            status=TIMEOUT,
            expected=expected,
            actual=normalize_output(_decode(error.stdout)),
            stderr=normalize_output(_decode(error.stderr)),
        )

    actual = normalize_output(_decode(completed.stdout))
    stderr = normalize_output(_decode(completed.stderr))
    if completed.returncode != 0:
        status = RUNTIME_ERROR
    elif actual != expected:
        status = WRONG_ANSWER
    else:
        status = PASS
    return CaseResult(case.name, status, expected, actual, stderr)


def run_problem(problem_dir: Path, timeout: float = 2.0) -> RunSummary:
    """Run every discovered case for a problem directory."""

    if timeout <= 0:
        raise ConfigError("timeout must be greater than zero")
    resolved_dir = Path(problem_dir).resolve()
    cases = discover_cases(resolved_dir)
    return RunSummary(
        tuple(run_case(resolved_dir, case, timeout) for case in cases),
    )


def _print_result(result: CaseResult) -> None:
    print(f"[{result.status}] {result.name}")
    if result.status == WRONG_ANSWER:
        print(f"  expected: {result.expected!r}")
        print(f"  actual:   {result.actual!r}")
    elif result.status == RUNTIME_ERROR:
        print(f"  stderr: {result.stderr or '(empty)'}")
    elif result.status == TIMEOUT:
        print("  process exceeded the configured timeout")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run an ACM solution against every tests/*.in and tests/*.out pair.",
    )
    parser.add_argument("problem_dir", type=Path, help="problem directory containing main.py")
    parser.add_argument(
        "--timeout",
        type=float,
        default=2.0,
        help="timeout per test case in seconds (default: 2.0)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        summary = run_problem(args.problem_dir, timeout=args.timeout)
    except ConfigError as error:
        print(f"[CONFIG_ERROR] {error}", file=sys.stderr)
        return 2

    for result in summary.results:
        _print_result(result)
    passed_count = sum(result.status == PASS for result in summary.results)
    print(f"\n{passed_count}/{len(summary.results)} cases passed")
    return 0 if summary.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())


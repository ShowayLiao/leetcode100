# Python ACM Practice Repository

## Scope

- Use Python for every solution in this repository.
- Write complete ACM-style programs that read standard input and write standard output.
- Keep solution code behind a `solve()` function and call it from an `if __name__ == "__main__"` entry point.
- Prefer the Python standard library. Add a dependency only after the user explicitly approves it.
- Treat each `problem.md` as the local input/output contract for that problem.

## Problem source and ordering

- If the user does not specify a problem source, default to the LeetCode Hot 100.
- Use [`sets/leetcode_hot100.md`](sets/leetcode_hot100.md) as the source of truth for the Hot 100 scope, local solving order, progress, and links. Update that file whenever a Hot 100 problem is added or its local status changes.
- Store newly added Hot 100 problems separately under `problems/hot100/`, and encode the repository's internal solving order separately from the original problem number: use `problems/hot100/<internal-order>_<four-digit-real-id>_<slug>/`, where `<internal-order>` starts at `01` and follows the local Hot 100 solving order, while `<four-digit-real-id>` preserves the actual LeetCode number. For example, internal item `01` for LeetCode 1 is `01_0001_two_sum`.
- Existing problem directories under `problems/leetcode/` are historical records and do not need to be renamed or moved solely because Hot 100 receives its separate directory.

## Judge workflow

When the user asks to judge, check, or review a solution:

1. Read the problem's `problem.md`, `main.py`, and all local test cases.
2. Confirm that the input format, output format, and constraints are sufficiently clear.
3. Confirm that the problem has at least 8 complete local test-case pairs under `tests/`.
4. Run all local tests before reporting a result.
5. Check correctness, parsing, formatting, time complexity, space complexity, and Python-specific risks.
6. Try edge cases such as minimum sizes, maximum values, duplicates, negative values, empty-like inputs allowed by the contract, and degenerate structures.
7. Give a minimal counterexample for each suspected correctness bug.

Report only evidence available locally. Never describe a local pass as an official AC. Use one of these conclusions:

- Current local tests pass; no counterexample was found by static review.
- Counterexample found.
- Runtime error.
- Timeout or complexity risk.
- Output format error.
- Insufficient problem constraints or tests to determine correctness.

Do not change the learner's `main.py` during judging unless the user explicitly asks for a fix or implementation.

## Coaching workflow

- Preserve the learner's attempt and reasoning.
- Start with a directional hint: a useful observation, data structure, or algorithm family.
- If requested, give a stronger hint describing state, invariants, or major steps.
- Next, offer pseudocode or a focused code fragment.
- Give a complete solution only when the user explicitly asks for the answer, implementation, or direct fix.
- Prefer questions and counterexamples that help the learner find the issue.
- When fixing a bug, add a regression case that demonstrates the bug before changing the implementation.

## Repository conventions

- Hot 100 path: `problems/hot100/<internal-order>_<four-digit-real-id>_<slug>/`.
- Explicitly sourced general LeetCode path: `problems/leetcode/<four-digit-id>_<slug>/`; existing paths using this format remain valid.
- Company path: `problems/company/<company>/<session>/<qNN>_<slug>/`.
- Use lowercase ASCII names with underscores for generated path segments.
- A problem directory contains `problem.md`, `main.py`, `notes.md`, and `tests/`.
- Every new `problem.md` must state the source URL, difficulty, problem type/tags, local ACM-style input/output contract, constraints, and at least one example or local test reference.
- A test case is a matching pair such as `tests/01.in` and `tests/01.out`.
- Every problem must have at least 8 complete test-case pairs in its `tests/` directory. Tests should cover normal cases and, where applicable, boundary sizes, maximum values, duplicates, negative values, empty-like inputs, and degenerate structures.
- Keep source URLs and personal summaries. Do not bulk-copy problem statements or solutions when their license is unclear.
- Do not add debug text to standard output.
- Run `python -m unittest discover -s tests -v` after changing repository tools.
- Run the affected problem through `python tools/run_tests.py <problem-directory>` after changing a solution.

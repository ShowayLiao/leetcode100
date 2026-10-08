"""ACM template: a case count, then a size and integer array per case."""

import sys


def solve() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    try:
        case_count = int(next(tokens))
    except StopIteration:
        return

    _cases: list[list[int]] = []
    for _ in range(case_count):
        size = int(next(tokens))
        _cases.append([int(next(tokens)) for _ in range(size)])
    # Compute and print each answer here.


if __name__ == "__main__":
    solve()


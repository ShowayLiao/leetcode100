"""ACM template: row count, column count, then a dense integer matrix."""

import sys


def solve() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    try:
        rows = int(next(tokens))
        columns = int(next(tokens))
    except StopIteration:
        return

    _matrix = [
        [int(next(tokens)) for _ in range(columns)]
        for _ in range(rows)
    ]
    # Compute and print the answer here.


if __name__ == "__main__":
    solve()


"""ACM template: treat every non-empty input line as one integer case."""

import sys


def solve() -> None:
    _cases = [
        list(map(int, line.split()))
        for line in sys.stdin.buffer
        if line.strip()
    ]
    # Compute and print one answer per case here.


if __name__ == "__main__":
    solve()


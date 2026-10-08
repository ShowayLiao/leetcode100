"""ACM template: one size followed by one integer array."""

import sys


def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    size = int(tokens[0])
    _numbers = list(map(int, tokens[1 : 1 + size]))
    # Compute and print the answer here.


if __name__ == "__main__":
    solve()


"""ACM template: node count, edge count, then undirected one-based edges."""

import sys


def solve() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    try:
        node_count = int(next(tokens))
        edge_count = int(next(tokens))
    except StopIteration:
        return

    _graph: list[list[int]] = [[] for _ in range(node_count + 1)]
    for _ in range(edge_count):
        left = int(next(tokens))
        right = int(next(tokens))
        _graph[left].append(right)
        _graph[right].append(left)
    # Compute and print the answer here.


if __name__ == "__main__":
    solve()


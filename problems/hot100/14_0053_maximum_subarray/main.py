import sys


def solve() -> None:
    # TODO: 按 problem.md 读取输入并完成练习。
    
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    vals = list(map(int,data[1:]))

    dp = [0 for _ in range(n)]

    dp[0] = vals[0]

    ans = dp[0]

    for i in range(n):

        dp[i] = max(vals[i]+dp[i-1],vals[i])

        ans = max(dp[i],ans)

    print(ans)


if __name__ == "__main__":
    solve()

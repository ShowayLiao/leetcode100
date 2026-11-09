import sys


def solve() -> None:
    # TODO: 按 problem.md 读取输入并完成练习。

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    left = None

    right = None

    vals = sorted((int(data[i]),int(data[i+1])) for i in range(1,2*n+1,2))

    ans = []

    for v in vals:

        cl,cr = v

        if left is None:
            left,right = cl,cr

            continue

        if cl>right:

            ans.append((left,right))
            left,right = cl,cr

        else:

            right = cr if cr>=right else right


    ans.append((left,right))


    print(len(ans))

    for a in ans:

        print(*a)





if __name__ == "__main__":
    solve()

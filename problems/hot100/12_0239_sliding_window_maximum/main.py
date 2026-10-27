import sys

from collections import deque


def solve() -> None:
    # TODO: 按 problem.md 读取输入并完成练习。
    
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    k = int(data[1])

    vals = list(map(int,data[2:]))

    queue = deque([])

    ans = []

    for i,v in enumerate(vals):

        while queue and vals[queue[-1]]<v:
            queue.pop()

        queue.append(i)

        if queue[0]<=i-k:

            queue.popleft()

        if i+1>=k:

            ans.append(vals[queue[0]])


    print(*ans)
        

        

        

    




if __name__ == "__main__":
    solve()

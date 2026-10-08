import sys

def solve()->None:

    n = int(sys.stdin.readline())
    strs = [sys.stdin.readline().strip("\r\n") for _ in range(n)]

    if n==0:
        print(0)
        return

    if n==1:
        print(1)
        print(strs[0])
        return

    seen:dict[str,list] = {}

    for ch in strs:

        key = "".join(sorted(ch))

        seen.setdefault(key,[]).append(ch)

    group = []

    for chs in seen.values():
        group.append(sorted(chs))

    group.sort()

    print(len(group))

    for i in range(len(group)):
        print(*group[i])






if __name__ == "__main__":
    solve()
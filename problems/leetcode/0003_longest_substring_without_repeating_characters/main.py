import sys

def solve()->None:

    s = input()

    seen = set()

    left = 0

    best = 0

    for index, ch in enumerate(s):

        while ch in seen:
            seen.remove(s[left])# 不能是remove ch因为要逐个检查
            left+=1

        seen.add(ch)

        best = max(best,(index-left+1))

    print(best)


if __name__ == "__main__":
    solve()


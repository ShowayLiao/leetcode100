import sys


def solve()->None:

    data = sys.stdin.read().splitlines()

    if not data :
        return

    s = data[0]

    seen = set()

    start = 0

    ans = 0

    for c in s:

        while c in seen:

            seen.remove(s[start])
            start+=1

        seen.add(c)

        ans = max(len(seen),ans)

    print(ans)








if __name__ =="__main__":
    solve()
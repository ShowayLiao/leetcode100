import sys
from collections import Counter


def solve() -> None:

    data = sys.stdin.read().splitlines()

    if not data:
        return

    s = data[0]

    t = data[1]

    need = Counter(t)

    windows = {}

    valid = 0

    start = 0

    left = 0

    best_len = len(s)+1

    for i,c in enumerate(s):

        if c in need:
            windows[c] = windows.get(c,0)+1

            if windows[c]==need[c]:
                valid+=1

        while valid==len(need):

            lenth = i-left+1

            if lenth<best_len:

                best_len = lenth
                start = left

            left+=1

            if s[left-1] in windows:

                if windows[s[left-1]]==need[s[left-1]]:
                    valid-=1

                windows[s[left-1]]-=1


    if best_len>len(s):
        print(

        )

    else:

        print(s[start:start+best_len])








if __name__ == "__main__":
    solve()
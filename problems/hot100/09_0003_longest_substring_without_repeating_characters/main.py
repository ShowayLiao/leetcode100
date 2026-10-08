import sys


def solve()->None:

    s = sys.stdin.readline().rstrip("\r\n")

    start = 0

    seen = set()

    max_len = 0

    for end,ch in enumerate(s):
        while ch in seen:
            seen.remove(s[start])
            start+=1

        seen.add(ch)

        max_len = max(max_len,end-start+1)

    print(max_len)








if __name__ =="__main__":
    solve()
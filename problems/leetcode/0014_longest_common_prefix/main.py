import sys


def solve()->None:
    n = int(sys.stdin.readline())
    strs = [sys.stdin.readline().rstrip("\r\n") for _ in range(n)]

    first_str = strs[0]
    others = strs[1:]

    for i,ch in enumerate(first_str):
        if any(i>=len(s) or s[i]!=ch for s in others):
            print(first_str[:i])
            return

    print(first_str)



if __name__ =="__main__":
    solve()



    


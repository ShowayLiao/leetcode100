import sys


def solve()->None:

    data = sys.stdin.read().splitlines()

    if not data :
        return

    s = data[0]

    seen = set()

    left = 0

    lenth = 0

    for i,c in enumerate(s):

        while c in seen:

            seen.remove(s[left])
            left+=1

        seen.add(c)

        lenth = max(lenth,i-left+1)


    print(lenth)
    








if __name__ =="__main__":
    solve()
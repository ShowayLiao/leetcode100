import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    t = int(data[1])

    values = list(map(int,data[2:]))

    sum = 0

    prefix = {0:1}

    ans = 0

    for v in values:

        sum+=v

        pre = prefix.get(sum-t,None)

        if pre is not None:
            ans+=pre

        prefix[sum] = prefix.get(sum,0)+1


    print(ans)

        




if __name__ == "__main__":
    solve()
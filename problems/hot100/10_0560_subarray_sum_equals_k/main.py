import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    prefix = {0:1}

    n = int(data[0])

    t = int(data[1])

    vals = list(map(int,data[2:]))

    total = 0

    ans = 0

    for i,v in enumerate(vals):

        total+=v

        ib = prefix.get(total-t,None)

        if ib is not None:
            ans+=ib

        prefix[total] = prefix.get(total,0)+1


    print(ans)
            


        




if __name__ == "__main__":
    solve()
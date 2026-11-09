import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    vals = list(map(int,data[1:]))

    uni = set(vals)

    best = 1

    for v in vals:

        if v-1 in uni:
            continue

        lenth = 1

        while v+1 in uni:
            lenth+=1
            v+=1
            best = max(best,lenth)

    print(best) 






if __name__ =="__main__":

    solve()
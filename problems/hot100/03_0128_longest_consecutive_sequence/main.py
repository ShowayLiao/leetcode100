import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    vs = list(map(int,data[1:]))

    uni = list(set(vs))

    bl = 1

    for v in vs:

        if v-1 in uni:
            continue

        l = 1

        while v+1 in uni:

            l+=1

            bl = max(bl,l)

            v+=1

    print(bl)
    






if __name__ =="__main__":

    solve()
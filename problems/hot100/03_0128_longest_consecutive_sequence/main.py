import sys

def solve()->None:

    n = int(sys.stdin.readline())

    nums = list(map(int,sys.stdin.readline().split()))

    values = set(nums)

    max_len = 0

    for v in values:
        if v-1 in values:
            continue

        len = 1

        while v+len in values:
            len+=1

        max_len = max(len,max_len)


    print(max_len)

    






if __name__ =="__main__":

    solve()
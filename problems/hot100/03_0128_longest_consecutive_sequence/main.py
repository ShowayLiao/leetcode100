import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    nums = list(map(int,data[1:]))

    uni = list(set(nums))

    ans = 1

    if len(nums)==0:
        print(0)
        return

    for d in nums:

        if d-1 in uni:
            continue

        count = 1

        while d+1 in uni:
            count+=1
            d+=1
            ans = max(ans,count)

    print(ans)
    






if __name__ =="__main__":

    solve()
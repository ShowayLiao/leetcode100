import sys

def solve()->None:
    n,target = map(int,input().split())
    nums = list(map(int,input().split()))
    seen: dict[int,int] = {}

    for index,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            print(seen[complement],index)

        seen[num]=index




        

if __name__ =="__main__":
    solve()

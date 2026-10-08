import sys


def solve()->None:
    n,target = map(int,sys.stdin.readline().split())
    nums = list(map(int,sys.stdin.readline().split()))

    seen:dict[int,int] = {

    }

    for i,num in enumerate(nums):
        complement = target-num

        if complement in seen:
            print(seen[complement],i)
            return

        seen[num]= i


    
    





if __name__ == "__main__":
    solve()
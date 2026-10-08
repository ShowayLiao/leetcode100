import sys


def solve()->None:

    n = int(sys.stdin.readline())

    nums = list(map(int,sys.stdin.readline().split()))

    if n==0:

        print(0)
        return 

    left = 0

    right = n-1

    left_max = nums[left]

    right_max = nums[right]

    water = 0

    while left<right:
        if left_max<right_max:
            left+=1
            left_max = max(nums[left],left_max)
            water += left_max-nums[left]

        else:
            right-=1
            right_max = max(nums[right],right_max)
            water +=right_max-nums[right]



    print(water)

    





if __name__ =="__main__":
    solve()
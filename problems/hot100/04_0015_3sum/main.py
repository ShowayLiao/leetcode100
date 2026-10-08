import sys

def solve()->None:

    n = int(sys.stdin.readline())

    nums = list(map(int,sys.stdin.readline().split()))

    nums.sort()

    result = []

    for i,num in enumerate(nums):

        if i>0 and nums[i]==nums[i-1]:

            continue

        left = i+1

        right = n-1

        while left<right:
            total = num+nums[left]+nums[right]

            if total==0:
                result.append([num,nums[left],nums[right]])

                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1]:
                    left+=1

                while left<right and nums[right]==nums[right+1]:
                    right-=1


            else:
                left = left+1 if total<0 else left
                right = right-1 if total>0 else right

    


    print(len(result))

    for s in result:
        print(*s)








if __name__ =="__main__":
    solve()
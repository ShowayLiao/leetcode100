import sys

def solve()->None:

    n = int(sys.stdin.readline())

    nums = list(map(int,sys.stdin.readline().split()))

    nums = sorted(nums)

    result = []

    

    for i,num in enumerate(nums):
        
        if i>0 and nums[i]==nums[i-1]:
            continue

        if num>0:#因为循环到num为正时，已经不可能组成三元数和为0了
            break

        left = i+1
        right = n-1

        while left<right:
            total = num+nums[left]+nums[right]
            if total ==0:
                
                result.append((num,nums[left],nums[right]))# 先加入数组，而非先去重，因为会错误的将-1（num，left-1） -1（left） 2这类排除
                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1]:# 有结果后，再移动到与上次不同的地方
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right+=1
                
            else:

                left=left+1 if total<0 else left
                right=right-1 if total>0 else right

    if len(result)==0:
        print(0)
        return
    else:
        print(len(result))
        for tuple in result:
            print(*tuple)


if __name__=="__main__":
    solve()


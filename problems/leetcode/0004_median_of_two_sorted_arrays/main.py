import sys

def solve()->None:
    m,n = map(int,input().split())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))

    if m>n:
        nums1,nums2 = nums2,nums1
        m,n = n,m

    half = (m+n+1)//2

    left = 0

    right = m

    while left<=right:#二分算法在最小的数组上寻找新数组的集合

        i = (left+right)//2 

        j = half - i # 另外一个数组的集合自动确定了

        nums1_left = nums1[i-1] if i>0 else float("-inf")
        nums1_right = nums1[i] if i<m else float("inf")
        nums2_left = nums2[j-1] if j>0 else float("-inf")
        nums2_right = nums2[j] if j<n else float("inf")

        if nums1_left>nums2_right:
            right = i-1

        elif nums1_right<nums2_left:
            left = i+1

        else:

            if (m+n)%2==0:
                left_max = max(nums2_left,nums1_left)
                right_min = min(nums1_right,nums2_right)
                answer = (left_max+right_min)/2
                print(f"{answer:.5f}")

            else:
                answer = max(nums2_left,nums1_left)
                print(f"{answer:.5f}")

            return



if __name__=="__main__":
    solve()

    
import sys

def solve()->None:
    n1,n2 = map(int,input().split())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))

    carry = 0

    result = []

    for index in range(max(n1,n2)):
        a = nums1[index] if index<n1 else 0
        b = nums2[index] if index<n2 else 0

        total = a+b+carry

        result.append(total%10)

        carry = total//10

    if carry:
        result.append(carry)

    print(*result)




if __name__ == "__main__":
    solve()
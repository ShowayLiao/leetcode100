import sys

def solve()->None:

    n = int(sys.stdin.readline())

    nums = list(map(int,sys.stdin.readline().split()))

    write = 0

    for read in range(n):
        # 本质上write指向应该写入非0的地方
        # read指向遍历整个数组
        # 所以nums[write]在非零的时候写入nums[read]
        # 因为write比read始终要慢（遇到0不递增）
        # 所以read非零才这样做，把0元素全部甩到了尾巴
        if nums[read]!=0:
            nums[write],nums[read] = nums[read],nums[write]
            write+=1


    print(*nums)


            




if __name__ == "__main__":
    solve()
import sys

def solve()->None:

    n = int(sys.stdin.readline())

    height = list(map(int,sys.stdin.readline().split()))

    best_area = 0

    def area(left:int,right:int)->int:
        return min(height[left],height[right])*(right-left)

    left = 0

    right = n-left-1

    while left<right:

        best_area=max(best_area,area(left,right))

        if height[left]<height[right]:
            left+=1
        else:
            right-=1

    print(best_area)
        


if __name__ =="__main__":
    solve()

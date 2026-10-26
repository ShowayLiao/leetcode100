import sys


def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    heights = list(map(int,data[1:]))

    left = 0

    right = n-1

    left_max = heights[left]

    right_max = heights[right]

    water = 0

    while left<right:

        if left_max<right_max:
            left+=1
            left_max = max(left_max,heights[left])
            water+= left_max-heights[left]

        else:
            right-=1
            right_max = max(right_max,heights[right])
            water += right_max-heights[right]

    print(water)

    





if __name__ =="__main__":
    solve()
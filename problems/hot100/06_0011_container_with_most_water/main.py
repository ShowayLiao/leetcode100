import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    h = list(map(int,data[1:]))

    left = 0

    right = n-1

    water = min(h[left],h[right])*(right-left)

    while left<right:

        if h[left]<h[right]:

            left+=1

        else:
            right-=1

        water = max(water,min(h[left],h[right])*(right-left))

    print(water)
    
    

    





        




if __name__ =="__main__":
    solve()
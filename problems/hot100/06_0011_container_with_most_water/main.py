import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    h = list(map(int,data[1:]))

    left = 0

    right = n-1

    water = 0

    while left<right:

        

        if h[left]<h[right]:
            water = max(water,h[left]*(right-left))
            left+=1

        else:
            water = max(water,h[right]*(right-left))
            right-=1


    print(water)

    
    

    





        




if __name__ =="__main__":
    solve()
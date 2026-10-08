import sys


def solve()->None:

    x = sys.stdin.readline().strip()

    if int(x)<0:
        print("false")
        return

    left = 0
    right = len(x)-left-1

    while left<=right and x[left]==x[right]:
        left+=1
        right = len(x)-left-1

    
    print("true" if right<left else "false")

        



    






if __name__ =="__main__":
    solve()
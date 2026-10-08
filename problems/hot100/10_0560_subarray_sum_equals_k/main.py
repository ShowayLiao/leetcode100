import sys

def solve()->None:

    n,target = map(int,sys.stdin.readline().split())

    nums = list(map(int,sys.stdin.readline().split()))

    result = 0

    prefix = 0

    seen:dict[int,int] = {0:1}


    for num in nums:
        prefix+=num

        need = prefix-target

        result+=seen.get(need,0)

        seen[prefix] = seen.get(prefix,0)+1

    

    print(result)
        




if __name__ == "__main__":
    solve()
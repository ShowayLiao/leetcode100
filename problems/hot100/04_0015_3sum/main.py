import sys

def solve()->None:

    data = sys.stdin.read().split()

    n = int(data[0])

    values = list(map(int,data[1:]))

    vals = sorted(values)

    ans = []

    for i,d in enumerate(vals):

        if i>0 and vals[i]==vals[i-1]:
            continue


        left = i+1

        right = n-1

        t = -d

        while left<right:

            total = vals[left]+vals[right]

            if total==t:

                ans.append((d,vals[left],vals[right]))

                left+=1

                right-=1

                while left<right and vals[left]==vals[left-1]:
                    left+=1

                while left<right and vals[right]==vals[right+1]:
                    right-=1

            elif total>t:

                right-=1

            else:
                left+=1

    ans_n = len(ans)

    print(ans_n)

    if ans_n>0:
        for a in ans:
            print(*a)





    








if __name__ =="__main__":
    solve()
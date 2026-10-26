import sys

def solve()->None:

    data = sys.stdin.read().split()

    values = list(map(int,data[1:]))

    values = sorted(values)

    n = int(data[0])

    ans = []

    for i,d in enumerate(values):

        if i>0 and values[i]==values[i-1]:
            continue

        left = i+1

        right = n-1

        t_sum = -d

        while left<right:

            total = values[left]+values[right]

            if total==t_sum:

                ans.append((d,values[left],values[right]))

                left+=1

                right-=1

                while left<right and values[left]==values[left-1]:
                    left+=1

                while left<right and values[right]==values[right+1]:
                    right-=1

            elif total>t_sum:

                right-=1

            else:
                left+=1

    ans_n = len(ans)

    print(ans_n)

    if ans_n>0:
        for c in ans:

            print(*c)



    








if __name__ =="__main__":
    solve()
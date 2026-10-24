import sys

def solve()->None:

    data = sys.stdin.read().split()

    values = list(map(int,data[1:]))

    values = sorted(values)

    ans = []

    for i,d in enumerate(values):

        if i>0 and values[i]==values[i-1]:
            continue

        t_sum = -d

        left = i+1

        right = len(values)-1

        while left < right:

            total = values[left]+values[right]

            if total<t_sum:
                left+=1

            elif total>t_sum:
                right-=1

            else:
                ans.append((d,values[left],values[right]))

                left+=1

                right-=1

                while left<right and values[left]==values[left-1]:
                    left+=1

                while left<right and values[right]==values[right+1]:
                    right-=1


    n = len(ans)

    print(n)

    if n:
        for num in ans:
            print(*num)
    








if __name__ =="__main__":
    solve()
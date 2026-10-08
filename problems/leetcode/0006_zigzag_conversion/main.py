import sys

def solve()->None:

    s = input()

    num_rows = int(input())

    if num_rows ==1:
        print(s)

    output = [[] for _ in range(num_rows)]

    j = 0

    i = 0

    direction = 1

    for indecx, ch in enumerate(s):
        output[i].append(ch)

        i +=direction

        if i >=num_rows-1:
            direction = -1

        if i<=0:
            direction = 1


    print("".join("".join(row) for row in output))



if __name__ =="__main__":
    solve()
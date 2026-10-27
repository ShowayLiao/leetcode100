import sys

def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print()
        return


    values = list(map(int,data[1:]))

    read = 0

    write = 0

    for read in range(n):

        if values[read]!=0:
            values[read],values[write]=values[write],values[read]
            write+=1

    print(*values)


            




if __name__ == "__main__":
    solve()
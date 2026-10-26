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

    write = 0

    read = 0

    while read<n:

        if values[read]!=0:
            values[write],values[read] = values[read],values[write]
            write+=1
            read+=1
        else:
            read+=1

        
        


    print(*values)


            




if __name__ == "__main__":
    solve()
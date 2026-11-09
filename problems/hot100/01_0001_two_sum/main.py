import sys


def solve()->None:

    data = sys.stdin.read().split()

    if not data:

        return

    t = int(data[1])

    vals = list(map(int,data[2:]))

    sum_dict = {}

    for i,v in enumerate(vals):

        i_b = sum_dict.get(t-v,None)

        if i_b is not None:
            print(i_b,i)

            return

        sum_dict[v] = i

    



if __name__ == "__main__":
    solve()
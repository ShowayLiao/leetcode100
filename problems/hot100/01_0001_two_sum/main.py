import sys


def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])

    t_sum = int(data[1])

    values = list(map(int,data[2:]))

    nums_dict = {}

    for i,d in enumerate(values):

        i_b = nums_dict.get(t_sum-d,None)

        if i_b is not None:

            print(i_b,i)

            return

        nums_dict[d] = i

    


    




    
    





if __name__ == "__main__":
    solve()
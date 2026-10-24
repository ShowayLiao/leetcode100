import sys


def solve()->None:

    data = sys.stdin.read().split()

    if not data:

        return

    t_sum = int(data[1])

    values = list(map(int,data[2:]))

    index_dict = {}

    for i,d in enumerate(values):

        i_b = index_dict.get(t_sum-d,None)

        if i_b is not None:

            print(i_b,i)

            return

        index_dict[d] = i

    

    


    




    
    





if __name__ == "__main__":
    solve()
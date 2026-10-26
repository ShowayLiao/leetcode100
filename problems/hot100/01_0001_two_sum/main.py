import sys


def solve()->None:

    data = sys.stdin.read().split()

    if not data:

        return

    t = int(data[1])

    num_dict = {}

    for i,d in enumerate(data[2:]):

        d = int(d)

        i_b = num_dict.get(t-d,None)

        if i_b is not None:
            print(i_b,i)
            return


        num_dict[d] = i

    


    

    


    




    
    





if __name__ == "__main__":
    solve()
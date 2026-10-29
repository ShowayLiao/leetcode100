import sys


def solve()->None:

    data = sys.stdin.read().split()

    if not data:

        return

    t = int(data[1])

    vals = list(map(int,data[2:]))

    total_dict = {}

    for i,v in enumerate(vals):

        ib = total_dict.get(t-v,None)

        if ib is not None:
            print(ib,i)
            return


        total_dict[v] = i

    
    


    

    


    




    
    





if __name__ == "__main__":
    solve()
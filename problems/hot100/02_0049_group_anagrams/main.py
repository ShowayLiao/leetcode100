import sys



def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    ch_dict = {}

    

    for c in data[1:]:

        ch_dict["".join(sorted(c))] = ch_dict.get("".join(sorted(c)),[])

        ch_dict["".join(sorted(c))].append(c)


    ch_list = [sorted(c) for c in ch_dict.values()]

    ch_list = sorted(ch_list)

    n_ans = len(ch_list)

    print(n_ans)

    if n_ans>0:

        for c in ch_list:
            print(*c)


    




if __name__ == "__main__":
    solve()
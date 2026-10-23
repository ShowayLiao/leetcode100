import sys



def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    ch_dict = {}

    for c in data[1:]:

        ch_dict["".join(sorted(c))] = ch_dict.get("".join(sorted(c)),[])

        ch_dict["".join(sorted(c))].append(c)

    ch_list = [sorted(ch) for ch in ch_dict.values()]

    ch_list = sorted(ch_list)

    if n==0:
        print(0)
        return


    print(len(ch_list))

    for c in ch_list:
        print(*c)
    





if __name__ == "__main__":
    solve()
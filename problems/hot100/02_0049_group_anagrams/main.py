import sys



def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    ch_dict = {}

    for c in data[1:]:

        ch_dict["".join(sorted(c))] = ch_dict.get("".join(sorted(c)),[])

        ch_dict["".join(sorted(c))].append(c)


    ch_list = []

    for c in ch_dict.values():

        ch_list.append(sorted(c))

    ch_list = sorted(ch_list)

    print(len(ch_list))

    for c in ch_list:
        print(*c)

    




if __name__ == "__main__":
    solve()
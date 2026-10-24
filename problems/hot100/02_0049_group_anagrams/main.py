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

    n = len(ch_list)

    print(n)

    if n!=0:

        for l in ch_list:

            print(*l)

    




if __name__ == "__main__":
    solve()
import sys



def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    c_dict = {}

    for c in data[1:]:

        c_dict["".join(sorted(c))] = c_dict.get("".join(sorted(c)),[])
        c_dict["".join(sorted(c))].append(c)

    c_list = [sorted(d) for d in c_dict.values()]

    c_list = sorted(c_list)

    print(len(c_list))

    for c in c_list:
        print(*c)
        




if __name__ == "__main__":
    solve()
import sys

class Node:

    def __init__(self,val):
        self.val = val  
        self.next = None


def build_node(data:list,suffix:Node = None):

    dummy = Node(0)

    cur = dummy

    for d in data:

        cur.next = Node(int(d))

        cur = cur.next

    cur.next = suffix

    return dummy.next



def solve():

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    it = iter(data)

    def read_values():

        n = int(next(it))

        return [next(it) for _ in range(n)]

    a_values = read_values()

    b_values = read_values()

    s_values = read_values()

    share = build_node(s_values)

    a = build_node(a_values,share)

    b = build_node(b_values,share)

    p = a

    q = b


    while p!=q:

        p = p.next if p else b
        q = q.next if q else a

    if p is None and q is None:
        print(-1)
        return

    cur = a

    count = 0

    while cur!=p:
        cur = cur.next
        count+=1

    print(count)






    




if __name__ == "__main__":
    solve()

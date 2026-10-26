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

    na = int(data[0])

    values_a = list(map(int,data[1:1+na]))

    nb = int(data[1+na])

    values_b = list(map(int,data[2+na:2+na+nb]))

    share_n = int(data[2+na+nb])

    share_values = list(map(int,data[3+na+nb:]))

    share_head = build_node(share_values)

    heada = build_node(values_a,share_head)

    headb = build_node(values_b,share_head)

    p = heada

    q = headb

    while p is not q:

        p = p.next if p else headb
        q = q.next if q else heada

    if p is None:
        print(-1)
        return


    cur = heada

    ans = 0

    while cur is not q:

        cur = cur.next

        ans+=1

    print(ans)



    




if __name__ == "__main__":
    solve()

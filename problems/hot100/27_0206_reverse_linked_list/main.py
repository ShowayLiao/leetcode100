import sys
class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None

def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    pre = dummy

    for _,d in  enumerate(data):
        pre.next = Node(int(d))
        pre = pre.next


    return dummy.next

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    head = build_node(data[1:])

    pre = None

    cur = head

    while cur:

        nxt = cur.next

        cur.next = pre

        pre = cur

        cur = nxt

    head  = pre

    cur = head

    out = []

    while cur:

        out.append(cur.val)
        cur = cur.next

    if out:
        print(*out)

    else:

        print("empty")


        


if __name__ == "__main__":

    solve()

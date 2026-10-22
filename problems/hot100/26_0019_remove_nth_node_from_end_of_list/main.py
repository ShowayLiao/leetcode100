import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


def build_node(data:list)->Node:

    if data is None:
        return

    dummy = Node(0)
    pre = dummy

    for _,d in enumerate(data):

        pre.next = Node(int(d))
        pre = pre.next

    return dummy.next


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n = int(data[1])

    head = build_node(data[2:])

    dummy = Node(0)

    dummy.next = head

    slow = dummy

    fast = dummy

    for _ in range(n):

        fast = fast.next


    while fast:
        fast = fast.next
        pre = slow
        slow = slow.next

    pre.next = slow.next


    cur = dummy.next

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

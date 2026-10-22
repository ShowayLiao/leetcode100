import sys
class Node:

    def __init__(self,val):
        self.val = val  
        self.next = None


def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur =dummy

    for _,d in enumerate(data):
        cur.next = Node(int(d))
        cur = cur.next


    return dummy.next

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n1 = int(data[0])

    head1 = build_node(data[1:1+n1])

    n2 = int(data[1+n1])

    head2 = build_node(data[2+n1:])


    dummy = Node(0)

    cur = dummy

    while head1 and head2:

        if head1.val<head2.val:
            cur.next = head1
            head1 = head1.next

        else:
            cur.next = head2
            head2  = head2.next

        cur = cur.next

    cur.next = head1 if head1 else head2

    out = []

    cur = dummy.next

    while cur:
        out.append(cur.val)
        cur = cur.next

    if out:
        print(*out)
    else:
        print("empty")


if __name__ == "__main__":
    solve()

import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None
        self.pre = None


def build_node(data:list)->tuple[Node,Node]:

    if not data:
        return None,None


    dummy = Node(0)

    cur = dummy

    pre = None

    for d in data:

        cur.next = Node(int(d))

        pre = cur

        cur = cur.next

        cur.pre = pre


    head = dummy.next

    head.pre = None

    tail = cur

    return head,tail


def solve():

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    head,tail = build_node(data[1:])

    if head is None or tail is None:
        print("true")
        return

    while head!=tail and head.pre!=tail:

        if head.val!=tail.val:
            print("false")
            return

        head = head.next
        tail = tail.pre


    print("true")


if __name__ == "__main__":
    solve()

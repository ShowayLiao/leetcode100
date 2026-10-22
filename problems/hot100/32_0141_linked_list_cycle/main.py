import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


    def __iter__(self):
        cur = self

        while cur is not None:
            yield cur
            cur = cur.next

def build_node(data:list,pos:int = -1)->Node:

    if not data:
        return

    dummy = Node(0)

    cur = dummy

    ring = None

    for i,d in enumerate(data):

        cur.next = Node(int(d))

        cur = cur.next

        if i == pos:
            ring = cur

    cur.next = ring

    return dummy.next


def solve():

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    pos = int(data[1])

    head = build_node(data[2:],pos)

    slow = head

    fast = head

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            break

    if fast is None or fast.next is None:

        print("false")

    else:

        print("true")


    

    


    




if __name__ == "__main__":
    solve()

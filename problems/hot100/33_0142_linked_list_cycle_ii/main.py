import sys

class Node:

    def __init__(self,val:int):
        self.val = val  
        self.next = None

def build_node(data:list,pos:int)->Node:

    if not data:
        return

    dummy = Node(0)

    cur =dummy

    ring_node = None

    for i,d in enumerate(data):
        cur.next = Node(int(d))
        cur = cur.next

        if i == pos:
            ring_node = cur

    cur.next = ring_node


    return dummy.next


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    pos = int(data[1])

    head = build_node(data[2:],pos)

    fast = head

    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break


    if fast is None or fast.next is None:
        print(-1)
        return

    cur = head

    count = 0

    while cur!=fast:

        count+=1
        cur = cur.next
        fast = fast.next

    print(count)




if __name__ == "__main__":
    solve()

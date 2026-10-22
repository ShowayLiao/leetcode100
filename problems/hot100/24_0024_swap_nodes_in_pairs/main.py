import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur =dummy

    for d in data:

        cur.next = Node(int(d))
        cur = cur.next

    return dummy.next

def reverse_two(head:Node)->Node:

    dummy = Node(0)

    dummy.next = head

    a = head

    b = head.next

    if b is None:
        return dummy.next

    pre = dummy

    while b:

        nxt = b.next

        b.next = a

        a.next = nxt

        pre.next = b

        pre = a

        a = nxt

        b = nxt.next if nxt else None

        





    return dummy.next





def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    head = build_node(data[1:])

    if head is None:
        print("empty")
        return

    head = reverse_two(head)

    cur =head

    out = []

    while cur:
        out.append(cur.val)
        cur = cur.next

    if out:
        print(*out)

    else:
        print("empty")

    

    
     




if __name__ =="__main__":

    solve()
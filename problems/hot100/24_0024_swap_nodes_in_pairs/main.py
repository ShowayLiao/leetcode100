import sys

class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

    def __iter__(self):
        cur = self

        while cur is not None:

            yield cur

            cur = cur.next



def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur = dummy

    for d in data:
        cur.next = Node(int(d))
        cur = cur.next

    return dummy.next

def solve():

    data = sys.stdin.read().split()

    if not data:
        return

    head = build_node(data[1:])

    if head is None:
        print("empty")
        return

    if head.next is None:
        print(head.val)
        return

    dummy = Node(0)

    dummy.next = head

    prev = dummy

    a = head

    b = head.next

    while a and b:

        nxt = b.next

        a.next = nxt

        b.next = a

        prev.next = b

        prev = a

        a = nxt

        if nxt:
            b = nxt.next

    out = [cur.val for cur in dummy.next]

    print(*out)
    

    
     




if __name__ =="__main__":

    solve()
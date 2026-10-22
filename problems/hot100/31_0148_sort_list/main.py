import sys
from typing import Optional

class Node:

    def __init__(self,val:int):
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


def split(head:Node)->tuple[Node,Node]:

    dummy = Node(0)

    dummy.next = head

    slow = dummy

    fast = dummy

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next

    next_head = slow.next

    slow.next = None

    return dummy.next,next_head


def sort_two(a:Node,b:Node)->Node:

    dummy = Node(0)

    cur = dummy

    while a and b:

        if a.val<b.val:
            cur.next = a
            a = a.next

        else:

            cur.next = b
            b = b.next

        cur = cur.next

    cur.next = a if a else b

    return dummy.next



def sort_list(head:Node)->Node:

    if head is None:
        return 

    if head.next is None:
        return head


    left_head,right_head = split(head)

    a = sort_list(left_head)

    b = sort_list(right_head)


    return sort_two(a,b)
    
    







    


def solve():

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])

    head = build_node(data[1:])


    cur = sort_list(head)

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

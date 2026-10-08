import sys
from typing import Optional

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


def build_list(data:list)->Node:

    if not data:
        return

    dummy = Node(0)
    cur = dummy

    for i,d in enumerate(data):

        cur.next = Node(int(d))
        cur = cur.next

    return dummy.next

def reverse_k_list(head:Node,k:int)->Node:

    dummy = Node(0)
    
    dummy.next = head

    pre_tail = dummy

    while True:

        cur  = pre_tail.next

        for _ in range(k):

            if cur is None:
                return dummy.next

            cur = cur.next

        next_head = cur

        pre = next_head

        cur = pre_tail.next

        old_head = cur

        for _ in range(k):

            nxt = cur.next

            cur.next = pre

            pre = cur
            cur = nxt

        pre_tail.next = pre
        pre_tail = old_head

        


def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])

    k = int(data[1])

    head = build_list(data[2:])

    head = reverse_k_list(head,k)

    cur = head

    out = []

    while cur:
        out.append(cur.val)
        cur = cur.next


    print(*out)

    
                


    


if __name__ == "__main__":


    solve()

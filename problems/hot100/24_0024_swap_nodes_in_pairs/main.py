import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


def build_tree(data:list)->Node:

    if data is None:
        return

    dummy = Node(0)

    cur = dummy

    for _,d in  enumerate(data):
        cur.next = Node(int(d))
        cur = cur.next

    return dummy.next


def reverse_two(head:Node)->Node:

    dummy = Node(0)
    dummy.next = head
    pre_tail = dummy

    while 1:

        
        cur = pre_tail.next

        for _ in range(2):
            if cur is None:
                return dummy.next
            cur = cur.next

        next_head = cur

        cur = pre_tail.next

        old_head = pre_tail.next

        pre = next_head

        for _ in range(2):

            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        pre_tail.next = pre
        pre_tail = old_head


        

    




def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n = int(data[0])

    if n == 0:
        print("empty")
        return

    head = build_tree(data[1:])

    head = reverse_two(head)

    cur = head

    out = []

    while cur:
        out.append(cur.val)
        cur = cur.next

    print(*out)

    

if __name__ == "__main__":
    solve()

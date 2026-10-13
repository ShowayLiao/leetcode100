import sys
class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None

def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    pre = dummy

    for _,d in  enumerate(data):
        pre.next = Node(int(d))
        pre = pre.next


    return dummy.next

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n = int(data[0])

    head = build_node(data[1:])

    if n == 0:
        print("empty")
        return

    if n == 1:
        print(head.val)
        return 

    pre = None
    cur = head


    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    cur = pre

    ans = []

    while cur:

        ans.append(cur.val)
        cur = cur.next

    print(*ans)



        


if __name__ == "__main__":

    solve()

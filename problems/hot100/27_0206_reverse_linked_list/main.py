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

    head = build_node(data[1:])

    if head is None:
        print("empty")
        return

    
    pre = None

    cur = head

    while cur:

        nxt = cur.next

        cur.next = pre

        pre = cur

        cur = nxt


    out = [node.val for node in pre]

    print(*out)
    



        


if __name__ == "__main__":

    solve()

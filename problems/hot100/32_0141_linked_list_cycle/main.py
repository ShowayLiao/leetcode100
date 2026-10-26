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

def build_node(data:list,pos:int)->Node:

    if not data:
        return

    dummy = Node(0)

    cur = dummy

    ring = None

    for i,d in enumerate(data):

        cur.next = Node(int(d))

        cur = cur.next

        if i==pos:

            ring = cur

    cur.next = ring

    return dummy.next



def solve()->None:

    data = sys.stdin.read().split()

    if not data:
        return


    pos = int(data[1])

    
    head = build_node(data[2:],pos)

    if head is None:
        print("false")
        return

    slow = head

    fast = head

    while fast and fast.next:

        fast = fast.next.next

        slow = slow.next

        if fast is slow:
            print("true")
            return

    print("false")


    


    




if __name__ == "__main__":
    solve()

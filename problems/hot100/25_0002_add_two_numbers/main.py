import sys

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None


def build_node(data:list)->Node:

    if data is None:
        return

    dummy = Node(0)

    pre = dummy

    for i,d in enumerate(data):

        pre.next = Node(int(d))

        pre = pre.next

    return dummy.next

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n1 = int(data[0])

    head1 = build_node(data[1:1+n1])

    n2 = int(data[1+n1])

    head2 = build_node(data[2+n1:])

    carry = 0

    cur1,cur2 = head1,head2

    out = []

    while cur1 or cur2 or carry:

        total = carry

        if cur1:
            total+=cur1.val
            cur1 = cur1.next

        if cur2:
            total+=cur2.val
            cur2 = cur2.next

        
        out.append(total%10)

        carry = total//10


    while len(out)>1 and out[-1]==0:
        out.pop()

    print(*out)




        

    
    


if __name__ == "__main__":

    solve()

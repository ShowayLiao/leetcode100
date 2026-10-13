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

    cur1 = head1

    cur2 = head2

    carry = 0

    ans = []

    while cur1 or cur2 or carry:

        total = carry

        if cur1:

            total+=cur1.val

            cur1 = cur1.next

        if cur2:

            total+=cur2.val

            cur2 = cur2.next

        
        ans.append(total%10)

        carry = total//10

    while len(ans)>1 and ans[-1]==0:
        ans.pop()

    print(*ans)





        

    
    


if __name__ == "__main__":

    solve()

import sys

class Node:

    def __init__(self,val:int,random = None,next = None):
        self.val = val
        self.random  = random
        self.next = next


    def __iter__(self):
        cur = self

        while cur is not None:
            yield cur
            cur =cur.next


def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur = dummy

    r_list = []

    heads = []

    for i in range(0,len(data),2):

        cur.next = Node(int(data[i]))

        cur = cur.next

        r_list.append(int(data[i+1]))
        heads.append(cur)

    for i,node in enumerate(heads):

        if r_list[i]==-1:
            continue

        node.random = heads[r_list[i]]


    return heads[0]


def deep_copy(head:Node):

    heads = []

    heads_dict = {node:i for i,node in enumerate(head)}

    r_list = []

    for node in head:
        heads.append(Node(node.val))
        r_list.append(heads_dict.get(node.random,-1))

    for i in range(len(heads)):

        if i!=len(heads)-1:

            heads[i].next = heads[i+1]

        if r_list[i]!=-1:

            heads[i].random = heads[r_list[i]]

    return heads
        


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n = int(data[0])

    head = build_node(data[1:])

    if n==0:
        print(0)
        return

    copy_heads = deep_copy(head)

    print(len(copy_heads))

    copy_dict = {node:i for i,node in enumerate(copy_heads)}

    for node in copy_heads:
        print(node.val,copy_dict.get(node.random,-1))



    

    


if __name__ == "__main__":
    solve()

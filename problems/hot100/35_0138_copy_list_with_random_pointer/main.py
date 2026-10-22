import sys

class Node:

    def __init__(self,val:int,random = None,next = None):
        self.val = val
        self.random  = random
        self.next = next


def build_node(data:list)->Node:
    if not data:
        return []

    it = iter(data)

    val = next(it,None)

    heads = []

    random_list = []

    pre = None

    while val is not None:

        node = Node(int(val))
        if pre:
            pre.next = node
        pre = node
        heads.append(node)
        random_list.append(int(next(it)))
        val = next(it,None)


    for i,node in enumerate(heads):

        node.random = heads[random_list[i]] if random_list[i]!=-1 else None


    return heads[0]

        


    
def deep_copy(head:Node)->list:

    if not head:
        return []

    copy_heads = []

    heads_dict = {}

    pre = None

    cur = head

    i = 0

    while cur:

        node = cur

        heads_dict[node]=i
        new_node = Node(node.val,node.random)
        if pre:
            pre.next = new_node

        pre = new_node
        copy_heads.append(new_node)

        cur = cur.next
        i+=1

    for node in copy_heads:

        i = heads_dict.get(node.random,-1)

        node.random = copy_heads[i] if i!=-1 else None

    return copy_heads

    
    


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    head = build_node(data[1:])


    copy_heads = deep_copy(head)


    if copy_heads:

        print(len(copy_heads))

        copy_dict = {node:i for i,node in enumerate(copy_heads)}

        for node in copy_heads:
            print(node.val,copy_dict.get(node.random,-1))



    else:

        print(0)

    


if __name__ == "__main__":
    solve()

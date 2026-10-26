import sys

class Node:

    def __init__(self,val:int,random = None,next = None):

        self.val = val

        self.random = random

        self.next = next

    def __iter__(self):

        cur = self

        while cur is not None:

            yield cur

            cur = cur.next


def build_node(data:list):

    if not data:

        return

    dummy = Node(0)

    cur = dummy

    heads = []

    r_list = []

    for i in range(0,len(data),2):

        cur.next = Node(int(data[i]))
        cur = cur.next

        heads.append(cur)
        r_list.append(int(data[i+1]))


    for i,node in enumerate(heads):

        if r_list[i]!=-1:

            node.random = heads[r_list[i]]

    return heads[0]


def deep_copy(head:Node):

    dummy = Node(0)

    cur =dummy

    heads = []

    node_dict = {}

    i = 0

    for node in head:

        cur.next = Node(node.val,node.random)
        cur = cur.next

        heads.append(cur)

        node_dict[node] = i

        i+=1

    for i,node in enumerate(heads):

        random = node_dict.get(node.random,-1)
        if random!=-1:
            node.random = heads[random]


    return heads
        







        


def solve():

    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    if n==0:
        print(0)
        return

    head = build_node(data[1:])

    new_heads = deep_copy(head)

    copy_dict = {node:i for i,node in enumerate(new_heads)}

    n = len(new_heads)

    print(n)

    if n!=0:

        for node in new_heads:
            print(node.val,copy_dict.get(node.random,-1))









    
        
        

        



    

    


if __name__ == "__main__":
    solve()

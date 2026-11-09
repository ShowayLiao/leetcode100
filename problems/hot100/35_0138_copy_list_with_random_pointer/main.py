import sys

class Node:

    def __init__(self,val:int,random=None,next = None):
        self.val = val
        self.random = random
        self.next = next

    def __iter__(self):
        cur = self

        while cur is not None:
            yield cur
            cur = cur.next


def build_node(data:list,n:int):

    heads = []

    r_list = []

    dummy = Node(0)

    cur =dummy

    for i in range(0,2*n,2):

        cur.next = Node(int(data[i]))

        cur = cur.next

        heads.append(cur)
        r_list.append(int(data[i+1]))


    for i in range(n):

        if r_list[i]==-1:
            continue

        heads[i].random = heads[r_list[i]]


    return dummy.next


def solve():

    data = sys.stdin.read().split()

    if not data:
        return

    if int(data[0])==0:
        print(0)
        return


    head = build_node(data[1:],int(data[0]))

    dummy = Node(0)

    cur = dummy

    i=0

    node_dict = {}

    heads = []

    for node in head:

        cur.next = Node(node.val,node.random)

        node_dict[node] = i

        i+=1

        cur = cur.next

        heads.append(cur)

    new_dict = {}

    i = 0

    for node in heads:

        index = node_dict.get(node.random,-1)

        if index!=-1:

            node.random = heads[index]

        new_dict[node] = i
        
        i+=1

    print(len(heads))


    for node in heads:

        print(node.val,new_dict.get(node.random,-1))






        








        
        



    

    


if __name__ == "__main__":
    solve()

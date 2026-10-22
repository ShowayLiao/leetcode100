import sys
import heapq

class Node:

    def __init__(self,val:int):
        self.val = val

        self.next = None



def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur =dummy


    for d in data:

        cur.next = Node(int(d))
        cur = cur.next


    return dummy.next

def merge_two(a:Node,b:Node)->Node:

    dummy = Node(0)

    cur = dummy

    while a and b:

        if a.val<b.val:
            cur.next = a
            a = a.next

        else:
            cur.next = b
            b = b.next

        cur = cur.next

    cur.next = a if a else b

    return dummy.next



def merge(heads:list,left:int,right:int)->Node:

    if left>right:
        return

    if left==right:
        return heads[left]


    mid = (left+right)//2


    a = merge(heads,left,mid)

    b = merge(heads,mid+1,right)

    return merge_two(a,b)





def solve(h:bool=False)->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    k = int(data[0])

    pos = 1

    heads = []

    heap = []

    out = []

    for i in range(k):

        n = int(data[pos])

        pos+=1

        node = build_node(data[pos:pos+n])

        if node:

            heads.append(node)

            heap.append((node.val,i,node))

        pos+=n


    if h:
        heapq.heapify(heap)

        while heap:
            _,i,node = heapq.heappop(heap)

            out.append(node.val)

            nxt = node.next

            if nxt:
                heapq.heappush(heap,(nxt.val,i,nxt))

    else:

        head = merge(heads,0,len(heads)-1)

        cur = head

        while cur :
            out.append(cur.val)

            cur = cur.next

    if out:
        print(*out)

    else:
        print("empty")






if __name__ == "__main__":
    solve(1)
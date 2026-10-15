import sys
import heapq


class Node:

    def __init__(self,val):
        self.val = val  
        self.next = None


def build_node(data:list)->Node:

    if not data:
        return

    dummy = Node(0)

    cur =dummy

    for _,d in enumerate(data):
        cur.next = Node(int(d))
        cur = cur.next


    return dummy.next


def merge_two(a:Node,b:Node)->Node:

    dummy = Node(0)

    cur =dummy

    while a and b:

        if a.val < b.val:
            cur.next = a
            a = a.next

        else:
            cur.next = b
            b = b.next

        cur = cur.next

    cur.next = a if a else b

    return dummy.next


def merge(heads:list,left:int,right:int)->Node:

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

    if k==0:
        print("empty")
        return

    pos = 1

    heads = []

    heap = []

    for i in range(k):

        n = int(data[pos])

        pos+=1

        node = build_node(data[pos:pos+n])

        heads.append(node)

        if node:
            heap.append((node.val,i,node))

        pos+=n

    dummy = Node(0)
    
    cur = dummy

    if h:

        heapq.heapify(heap)

        

        while heap:

            _,i,node = heapq.heappop(heap)

            cur.next = node

            cur = cur.next

            if cur.next:

                nxt = cur.next
                heapq.heappush(heap,(nxt.val,i,nxt))

    else:

        dummy.next = merge(heads,0,k-1)

    cur = dummy.next

    out = []

    while cur:
        out.append(cur.val)
        cur = cur.next

    if out:
        print(*out)

    else:
        print("empty")


if __name__ =="__main__":

    solve(0)
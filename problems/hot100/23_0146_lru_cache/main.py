import sys

from typing import Optional

class Node:

    def __init__(self,k:int,v:int):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None




class LRU_cache:

    def __init__(self,c:int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.lru_dict:dict[int:Node] = {}
        self.head.next = self.tail
        self.tail.pre = self.head
        self.c =c

    def _unlink(self,node:Node):
        if node:
            node.pre.next,node.next.pre = node.next,node.pre

    def _push(self,node:Node):

        if node:

            node.next = self.head.next

            node.pre = self.head

            self.head.next.pre,self.head.next = node,node

    def _touch(self,node:Node):

        self._unlink(node)
        self._push(node)

    def get(self,k:int):

        node = self.lru_dict.get(k,None)


        if node:
            self._touch(node)
            return node.v

        else:
            return -1


    def put(self,k:int,v:int):

        node = self.lru_dict.get(k,None)

        if node:

            node.v = v

            self._touch(node)

        else:

            node = Node(k,v)

            self._push(node)

            self.lru_dict[k] = node

        if len(self.lru_dict)>self.c:

            node = self.tail.pre

            self._unlink(node)

            del self.lru_dict[node.k]






def solve():

    lines = sys.stdin.buffer.read().splitlines()

    if not lines:
        return

    c,q = map(int,lines[0].split())

    lru = LRU_cache(c)

    for line in lines[1:]:

        data = line.split()

        if data[0]==b"put":

            lru.put(int(data[1]),int(data[2]))
            

        elif data[0]==b"get":

            v = lru.get(int(data[1]))
            print(v)



    
        





if __name__ == "__main__":
    solve()

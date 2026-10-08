import sys

from typing import Optional


class Node:
    def __init__(self,k:int,v:int):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None


class LRUcahce:
    def __init__(self,c:int):
        self.map:dict[int,Node] = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.c = c

    def _unlink(self,node:Node):

        node.pre.next,node.next.pre = node.next,node.pre
         

    def _push_front(self,node:Node):

        nxt = self.head.next

        self.head.next = node

        nxt.pre = node

        node.next = nxt
        node.pre = self.head

    def _touch(self,node:Node):

        self._unlink(node)
        self._push_front(node)


    def get(self,k:int)->int:

        node = self.map.get(k,None)

        if node:
            self._touch(node)
            return node.v
        else:
            return -1


    def put(self,k:int,v:int)->None:

        node = self.map.get(k,None)

        if node:
            self.map[k].v = v
            self._touch(node)

        else:

            node = Node(k,v)
            self.map[k] = node
            self._push_front(node)

        if len(self.map)>self.c:

            node = self.tail.pre
            self._unlink(node)
            del self.map[node.k]


def solve():

    data = sys.stdin.buffer.read().splitlines()

    if not data:
        return

    c,q = map(int,data[0].split())

    lru = LRUcahce(c)

    for i,line in enumerate(data[1:]):

        d = line.split()

        if d[0]==b"put":
            lru.put(int(d[1]),int(d[2]))

        elif d[0]==b"get":
            print(lru.get(int(d[1])))

        









if __name__ == "__main__":
    solve()

import sys
from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(data:list,n:int)->TreeNode:

    root = None

    if not data:
        return root

    stack = [(0,n,None,None)]

    while stack:

        l,r,parent,side = stack.pop()

        if l>=r:
            continue

        mid = (l+r)//2

        node = TreeNode(int(data[mid]))

        if parent is None:

            root = node

        elif side =="left":

            parent.left = node

        else:

            parent.right = node

        stack.append((l,mid,node,"left"))
        stack.append((mid+1,r,node,"right"))


    return root
    


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    root = build_tree(data[1:],int(data[0]))

    queue = deque([root])

    out = []

    while queue:

        level_size = len(queue)

        for _ in range(level_size):

            node = queue.popleft()

            if node:
                out.append(node.val)

            else:
                out.append("null")
                continue


            queue.append(node.left)
            queue.append(node.right)


    while out and out[-1]=="null":
        out.pop()

    print(*out)

    


if __name__ == "__main__":
    solve()


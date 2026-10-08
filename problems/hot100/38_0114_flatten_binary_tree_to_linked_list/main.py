import sys

from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(data:list):

    if not data:
        return

    root = TreeNode(data[0])

    queue = deque([root])

    index = 1

    while queue and index<len(data):

        node = queue.popleft()

        if data[index] !="null":

            node.left = TreeNode(data[index])

            queue.append(node.left)

        index+=1


        if index<len(data) and data[index]!="null":

            node.right = TreeNode(data[index])

            queue.append(node.right)

        index+=1


    return root


def solve()->None:

    n = int(sys.stdin.readline())

    data = sys.stdin.readline().split()

    if n==0:
        print([])

        return

    root = build_tree(data)

    stack = [(root,False)]

    pre = None

    while stack:

        node,visit = stack.pop()

        if node is None:
            continue

        if not visit:

            stack.append((node.right,False))
            stack.append((node.left,False))
            stack.append((node,True))

        else:

            if pre:
                pre.right = node
                pre.left = None
            pre = node

    cur = root

    out = []

    while cur:
        out.append(cur.val)
        cur = cur.right

    print(*out)
            

if __name__ == "__main__":
    solve()


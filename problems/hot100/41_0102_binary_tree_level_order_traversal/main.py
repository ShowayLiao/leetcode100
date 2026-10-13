import sys

from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(vals:list):

    if not vals or vals[0]==b"null":
        return

    root = TreeNode(int(vals[0]))

    queue = deque([root])

    index = 1

    while index<len(vals) and queue:

        node = queue.popleft()

        if node is None:
            continue

        if vals[index]!=b"null":
            node.left = TreeNode(int(vals[index]))
            queue.append(node.left)

        index+=1

        if index<len(vals) and vals[index]!=b"null":
            node.right = TreeNode(int(vals[index]))
            queue.append(node.right)

        index+=1

    return root


def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])

    root = build_tree(data[1:])

    queue = deque([root])

    while queue:

        level_size = len(queue)

        out = []

        for _ in range(level_size):

            node = queue.popleft()

            out.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


        print(*out)

    

    


    



if __name__ == "__main__":

    solve()


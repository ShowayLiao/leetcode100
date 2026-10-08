import sys

from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(data:list)->TreeNode:

    if not data:

        return

    root = TreeNode(int(data[0]))

    queue = deque([root])

    index = 1

    while index<len(data) and queue:

        node = queue.popleft()

        if data[index]!=b"null":
            node.left = TreeNode(int(data[index]))
            queue.append(node.left)

        index+=1

        if index<len(data) and data[index]!=b"null":
            node.right = TreeNode(int(data[index]))
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

    out = []

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            node = queue.popleft()

            if i == level_size-1:
                out.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


    print(*out)

    


if __name__ == "__main__":
    solve()


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

    while queue and index<len(data):

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

    stack = [(root.left,root.right)]

    while stack:

        left,right = stack.pop()

        if left is None and right is None:
            continue

        elif left is None or right is None:
            print("false")
            return

        if left.val != right.val:
            print("false")
            return

        stack.append((left.left,right.right))
        stack.append((left.right,right.left))

    print("true")
    



if __name__ == "__main__":
    solve()


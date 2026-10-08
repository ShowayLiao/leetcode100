import sys

from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(data:list)->TreeNode:

    if not data or data[0]==b"null":
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

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    # TODO: implement the ACM-style solution.

    n = int(data[0])

    root = build_tree(data[1:])

    if n==0:
        print("true")
        return

    if n==1:
        print("true")
        return

    stack = [(root,False)]

    pre = None

    while stack:

        node,visit = stack.pop()

        if node is None:
            continue

        if not visit:

            stack.append((node.right,False))
            stack.append((node,True))
            stack.append((node.left,False))

        else:

            if pre and pre.val>=node.val:
                print("false")
                return

            pre = node


    print("true")





if __name__ == "__main__":
    solve()


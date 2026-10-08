import sys

from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(vals:list)->TreeNode:

    root = None

    if not vals or vals[0]==b"null":
        return root

    root = TreeNode(int(vals[0]))

    queue = deque([root])

    index = 1

    while index < len(vals) and queue:

        node = queue.popleft()

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

    if n==1:
        print(0)
        return

    if n==2:
        print(1)
        return

    stack = [(root,False)]

    lenth = {}

    ans = 0

    while stack:

        node,visit = stack.pop()

        if node is None:

            continue


        if not visit:

            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))

        else:

            left = lenth.get(node.left,-1)
            right = lenth.get(node.right,-1)

            ans = max(ans,left+right+2)

            lenth[node] = max(left+1,right+1)

    print(ans)
    




if __name__ == "__main__":
    solve()


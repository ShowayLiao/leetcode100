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

        if index < len(data) and data[index]!=b"null":

            node.right = TreeNode(int(data[index]))
            queue.append(node.right)


        index+=1


    return root


def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:

        return

    k = int(data[1])

    root = build_tree(data[2:])

    stack = [(root,False)]

    conut = 0


    while stack:

        node,visit = stack.pop()

        if node is None:
            continue


        if not visit:

            stack.append((node.right,False))
            stack.append((node,True))
            stack.append((node.left,False))

        else:

            conut+=1

            if conut==k:
                print(node.val)

                return









        


if __name__ == "__main__":

    solve()
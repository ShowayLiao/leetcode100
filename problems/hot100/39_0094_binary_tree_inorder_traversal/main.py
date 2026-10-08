import sys
from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None

def build_tree(data:list)->TreeNode:

    root = TreeNode(data[0])

    queue = deque([root])

    index = 1

    while queue and index<len(data):

        cur = queue.popleft()

        if data[index]!="null":
            cur.left = TreeNode(data[index])  
            queue.append(cur.left)

        index+=1

        if index<len(data) and data[index]!="null":
            cur.right = TreeNode(data[index])
            queue.append(cur.right)


        index+=1

    return root


def solve()->None:

    n = int(sys.stdin.readline())

    data = sys.stdin.readline().split()

    if n==0:
        print([])
        return

    for i,d in enumerate(data):

        if d == "null":
            continue

        data[i] = int(d)


    root = build_tree(data)


    stack = [(root,False)]

    out = []

    while stack:

        node,visit = stack.pop()

        if node is None:
            continue

        if not visit:

            stack.append((node.right,False))
            stack.append((node,True))
            stack.append((node.left,False))

        else:

            out.append(node.val)


    print(*out)



    

    
    


if __name__ == "__main__":
    solve()


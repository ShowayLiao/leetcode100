import sys
from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None



def build_tree(data:list)->None:

    if not data:

        return

    root = TreeNode(data[0])

    queue = deque([root])

    index= 1

    while queue and index<len(data):

        node = queue.popleft()

        if data[index]!="null":

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

    for i,d in enumerate(data):
        if d=="null":
            continue

        data[i] = int(d)

    root = build_tree(data)

    stack = [(root,False)]

    sum ={}

    ans = float("-inf")

    while stack:

        node,visit = stack.pop()

        if node is None:
            continue

        if not visit:

            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))

        else:

            left = max(sum.get(node.left,0),0)
            right = max(sum.get(node.right,0),0)

            ans = max(ans,left+right+node.val)

            sum[node] = max(left+node.val,right+node.val)
            

    print(ans)







if __name__ =="__main__":
    solve()
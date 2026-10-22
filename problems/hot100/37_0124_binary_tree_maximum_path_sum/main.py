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

    root = build_tree(data[1:])

    stack = [(root,False)]

    path_sum = {}

    ans= float("-inf")

    while stack:

       node,visit = stack.pop()

       if node is None:
           continue

       if not visit:

           stack.append((node,True))
           stack.append((node.right,False))
           stack.append((node.left,False))


       else:

           left = max(path_sum.get(node.left,0),0)
           right = max(path_sum.get(node.right,0),0)

           ans = max(ans,left+right+node.val)

           path_sum[node] = max(left+node.val,right+node.val)

    
    
    
    print(ans)







if __name__ =="__main__":
    solve()
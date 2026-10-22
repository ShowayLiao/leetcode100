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

    targetSum = int(data[1])

    root = build_tree(data[2:])

    stack = [(root,0,False)]

    prefix = {0:1}

    ans = 0

    while stack:

        node,pre,visit = stack.pop()

        if node is None:

            continue

        if not visit:

            total = pre+node.val

            ans+=prefix.get(total-targetSum,0)

            prefix[total] = prefix.get(total,0)+1

            stack.append((node,total,True))

            stack.append((node.right,total,False))

            stack.append((node.left,total,False))

        else:

            prefix[pre]-=1

            if prefix[pre]==0:
                del prefix[pre]

    print(ans)




            

            
            
            

            


            


if __name__ == "__main__":
    solve()


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

    path_sum = {0:1}

    answer = 0

    while stack:

        node,pre,visit = stack.pop()

        if node is None:
            continue


        if not visit:

            cur = pre+node.val

            answer += path_sum.get(cur-targetSum,0)

            path_sum[cur] = path_sum.get(cur,0)+1

            stack.append((node,cur,True))
            stack.append((node.right,cur,False))
            stack.append((node.left,cur,False))

        else:

            path_sum[pre]-=1

            if path_sum[pre]==0:

                del path_sum[pre]


    print(answer) 

            
            
            

            


            


if __name__ == "__main__":
    solve()


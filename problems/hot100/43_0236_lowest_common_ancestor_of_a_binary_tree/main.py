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

    p = int(data[1])

    q = int(data[2])

    root = build_tree(data[3:])

    stack = [(root,False)]

    found = {}

    while stack:

        node,visit = stack.pop()

        if node is None:
            continue

        if not visit:

            stack.append((node,True))
            stack.append((node.right,False))
            stack.append((node.left,False))

        else:

            left_p,left_q = found.get(node.left,(0,0))
            right_p,right_q = found.get(node.right,(0,0))

            found_p = left_p or right_p or node.val==p
            found_q = right_q or left_q or node.val==q

            if found_p and found_q:
                print(node.val)
                return

            found[node] = (found_p,found_q)


    
            


    

        




if __name__ == "__main__":


    solve()


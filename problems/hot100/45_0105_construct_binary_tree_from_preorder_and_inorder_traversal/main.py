import sys


from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None

def build_tree(pdata:list,idata:list,n:int)->TreeNode:

    if not pdata or not idata:
        return

    root = None

    stack = [(0,n,0,n,None,None)]

    i_pos = {int(value):i for i,value in enumerate(idata)}

    while stack:

        pl,pr,il,ir,parent,side = stack.pop()

        if pl>=pr:
            continue

        node = TreeNode(int(pdata[pl]))

        if parent is None:
            root = node

        elif side == "left":
            parent.left = node

        else:
            parent.right = node


        mid = i_pos[node.val]

        left_n = mid-il

        stack.append((pl+1,pl+1+left_n,il,mid,node,"left"))
        stack.append((pl+1+left_n,pr,mid+1,ir,node,"right"))


    return root 


def solve()->None:

    data = sys.stdin.buffer.read().split()

    if not data:
        return

    n = int(data[0])

    root = build_tree(data[1:1+n],data[1+n:],n)

    queue = deque([root])

    out = []

    while queue:

        level_size = len(queue)

        for _ in range(level_size):

            node  = queue.popleft()

            if node:

                out.append(node.val)

            else:

                out.append("null")
                continue


            queue.append(node.left)
            queue.append(node.right)


    while out and out[-1]=="null":
        out.pop()
    

    print(*out)



    


if __name__ == "__main__":
    solve()


import sys


from collections import deque

class TreeNode:
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None

def build_tree(data_p:list,data_i:list,n:int)->TreeNode:

    root = None

    if not data_p or not data_i:
        return root

    i_pos = {int(value):i for i,value in enumerate(data_i)}

    stack = [(0,n,0,n,None,None)]

    while stack:

        pl,pr,il,ir,parent,side = stack.pop()

        if pl>=pr:
            continue

        node = TreeNode(int(data_p[pl]))

        if parent is None:
            root = node

        elif side == "left":
            parent.left = node

        else:
            parent.right = node


        mid = i_pos[node.val]

        left_size = mid - il

        stack.append((
            pl+1+left_size,pr,
            mid+1,ir,
            node,"right"
        ))

        stack.append((
            pl+1,pl+1+left_size,
            il,il+left_size,
            node,"left"
        ))

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

        for i in range(level_size):
            node = queue.popleft()

            if node is None:
                out.append("null")
                continue
            else:
                out.append(node.val)

            queue.append(node.left)
            queue.append(node.right)


    while out and out[-1]=="null":
        out.pop()

    print(*out)


if __name__ == "__main__":
    solve()


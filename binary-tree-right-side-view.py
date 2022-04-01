from collections import deque


class BinaryTree:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

def lot(tree):
    q = deque(tree)
    out = []

    while q:
        rightSide = None
        
        # Every node in the current level.
        qLen = len(q)

        for _ in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)

        if rightSide:
            out.append(rightSide.val)

    return out

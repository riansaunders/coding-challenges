class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def mergeTrees(a, b):
    if not a:
        return b
    if not b:
        return a
    
    v1 = a.val if a else 0
    v2 = b.val if b else 0

    res = TreeNode(val=v1+v2)
    res.left = mergeTrees(a.left if a else None, b.left if b else None)
    res.right = mergeTrees(a.right if a else None, b.right if b else None)

    return res


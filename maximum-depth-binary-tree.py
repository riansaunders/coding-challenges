from collections import deque


def md(root):

    def dfs(root):

        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        return max(left, right) + 1

    return dfs(root)

def mdlot(root):
    if not root:
        return 0
    level = 0
    q = deque([root])
    while q:

        qlen = len(q)
        for _ in range(qlen):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        level += 1
    return level
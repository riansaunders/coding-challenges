def mps(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0 

        leftMax = dfs(root.left)
        leftMax = max(leftMax, 0)

        rightMax = dfs(root.right)
        rightMax = max(rightMax, 0)

        # Value with the split (The left and right)
        res[0] = max(res[0], root.val + leftMax + rightMax)

        # Value without splitting both trees, taking the bigger of either one
        return root.val + max(leftMax, rightMax)

    dfs(root)

    return res[0]
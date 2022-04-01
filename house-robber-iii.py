def robber(root):

    # [withRoot, withoutRoot]
    def dfs(root):
        if not root:
            return [0, 0] 
            
        left = dfs(root.left)
        right = dfs(root.right)

        take = root.val + left[1] + right[1]
        notTake = max(left[0], right[0])

        return [take, notTake]

    return max(dfs(root))
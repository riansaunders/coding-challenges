def combosum(nums, t):
    dp = {}

    def dfs(total):
        if total == t:
            return 1
        if total in dp:
            return dp[total]
        if total > t:
            return 0
            
        res = 0
        for x in range(len(nums)):
            res += dfs(total + nums[x])
        dp[total] = res
        return res

    return dfs(0)

print(combosum([1,2,3], 4))


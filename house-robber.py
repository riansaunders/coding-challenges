def hr(nums):

    rob1, rob2 = 0, 0
    for n in nums:
        tmp = max(rob2, n + rob1)
        rob1 = rob2
        rob2 = tmp
    return rob2

    dp = {}

    def dfs(i):
        if i == len(nums):
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max(nums[i],  nums[i] + dfs(i + 2))
        return dp[i]
    
    return dfs(0)

print(hr([1,2,3,1]))
def lis(nums):
    dp = [ 1 for _ in range(len(nums)) ]
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(1, dp[i], 1 + dp[j])
    return max(dp)

    dp = { len(nums) - 1: 1 }

    def dfs(i):
        if i in dp:
            return dp[i]
        if i == len(nums):
            return 0

        res = 1
        for j in range(i, len(nums)):
            if nums[j] > nums[i]:
                res = max(res, 1 + dfs(j))
        dp[i] = res

        return res

    res = 1
    for i in range(len(nums)):
        res = max(res, dfs(i))
    
    return res

print(lis([10,9,2,5,3,7,101,18]))
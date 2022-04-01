def mj(nums):

    dp = [float("inf") for _ in range(len(nums))]
    dp[0] = 0
    for i in range(len(nums) - 1):
        for j in range(1, min(len(nums), i + nums[i] + 1)):
            dp[j] = min(dp[j], dp[i] + 1) 
    return dp[-1]


    def dfs(i):
        if i + 1 >= len(nums):
            return 0 
        res = float("inf")

        for j in range(1, nums[i] + 1): 
            res = min(res, 1 + dfs(i + j))
        return res
    
    return dfs(0)


print(mj([2,1,1,1,4]))
# print(mj([1,1,3,6,9,3,0,1,3]))
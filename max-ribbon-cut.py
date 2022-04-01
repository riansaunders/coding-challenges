def mrc(nums, n):
    ni = -float("inf")

    dp = [ni for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(1, len(nums)):
        for j in range(1, n + 1): 
            dp[j] = max(dp[j], dp[j - 1])
            
            if j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + 1)
    return dp[-1]

    ni = -float("inf")

    dp = [ni for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = 1 if nums[0] == i else ni

    for i in range(1, len(nums)):
        for j in range(1, n + 1): 
            if j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + 1)

    return dp[-1]


    return dp[-1]

    dp = [[ni for _ in range(n + 1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = 0
    for i in range(1, n + 1):
        dp[0][i] = 1 if nums[0] == i else ni

    for i in range(len(nums)):
        for j in range(1, n + 1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]

            if j >= nums[i]:
                dp[i][j] = max(dp[i][j], dp[i][j - nums[i]] + 1)

    print(dp)

    return dp[-1][-1]


    def dfs(i, n):
        if n <= 0:
            return 0
        if i == len(nums) or n <= 0:
            return 0
        take = 0
        if nums[i] <= n:
            take = dfs(i, n - nums[i]) + 1 
        return max(take, dfs(i + 1, n))

    return dfs(0, n)

# print(mrc([2,3,5], 5))
print(mrc([2,3], 7))
# print(mrc([3,5,7] , 13))
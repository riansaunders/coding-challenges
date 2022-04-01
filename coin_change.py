import pprint


def count_change(nums, a):

    dp = [float("inf") for _ in range(a + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(1, a + 1):
        dp[i] = 1 if nums[0] == i else dp[i]
    
    for i in range(1, len(nums)):
        for j in range(1, a + 1):
            if j >= nums[i]:
                dp[j] = min(dp[j], dp[j - nums[i]] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1


    dp = [[float('inf') for _ in range(a + 1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = 0
    
    for i in range(1, a + 1):
        dp[0][i] = 1 if i == nums[0] else float("inf")
     
    for i in range(1, len(nums)):
        for j in range(1, a + 1):
            take = float("inf")
            if j >= nums[i]:
                take = dp[i - 1][j - nums[i]] + 1
            dp[i][j] = min(dp[i][j], take, dp[i - 1][j])
    

    return dp[-1][-1] if dp[-1][-1] != float("inf") else -1

    if a <= 0:
        return 0


    def dfs(i, a):
        if a == 0:
            return 0
        if i == len(nums):
            return float("inf")
        
        take = float("inf")
        if nums[i] <= a:
            take = dfs(i, a - nums[i]) + 1

        return min(take, dfs(i + 1, a))
    
    return dfs(0, a)


def main():
    print(count_change([1, 2, 3], 5))
    # print(count_change([1, 2, 3], 11))
    # print(count_change([1, 2, 3], 7))
    # print(count_change([3, 5], 7))


main()

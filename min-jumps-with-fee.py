def mjf(fees, n):

    # n = len(fees)
    # dp = [0 for x in range(n+1)]  # +1 to handle the 0th step
    # dp[0] = 0  # if there are no steps, we don't have to pay any fee
    # dp[1] = fees[0]  # only one step, so we have to pay its fee
    # # for 2 steps, since we start from the first step, so we have to pay its fee
    # # and from the first step we can reach the top by taking two steps, so
    # # we don't have to pay any other fee.
    # dp[2] = fees[0]

    # # please note that dp[] has one extra element to handle the 0th step
    # for i in range(2, n):
    #     dp[i + 1] = min(fees[i] + dp[i], 
    #                 fees[i - 1] + dp[i - 1], 
    #                 fees[i - 2] + dp[i - 2])
    # print(dp)
    # return dp[-1]


    dp = [float("inf") for _ in range(n + 1)]

    # The first 3 steps.
    # dp[0] = 0
    # dp[1] = fees[0]
    # dp[2] = fees[0] 
    # for i in range(2,n):
    #     dp[i + 1] = min(fees[i] + dp[i], fees[i - 1] + dp[i - 1], fees[i - 2] + dp[i - 2])
     
    # print(dp)
    # return dp[-1]


    def dfs(n):
        if n <= 1:
            return 0



        res = float("inf")
        for j in range(1,4):
            if j <= n:
                res = min(res, fees[n] + dfs(n - j))
        return res

    return dfs(n - 1)


print(mjf([1,2,5,2,1,2], 5))
print(mjf([2,3,4,5], 3))
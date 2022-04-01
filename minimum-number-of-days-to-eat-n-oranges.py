def oranges(n):
    dp = {}

    dp = { 0: 0, 1: 1, }

    # for i in range(1, )

    def dfs(i):
        if i in dp:
            return dp[i]


        twoDays = 1 + (i %2) +  dfs(i // 2) 
        threeDays = 1 + (i % 3) +  dfs(i // 3) 
        dp[i] = min(threeDays, twoDays)
        return dp[i]

    # def dfs(i):
    #     if i == 1:
    #         return 1
    #     if i in dp:
    #         return dp[i]
            

    #     dp[i] = 1
    #     threeDays = dfs(i - (2 * (i/3))) if i % 3 == 0 else float("inf")
    #     twoDays = dfs(i - (i / 2)) if i % 2 == 0 else float("inf")
    #     dp[i] += min(threeDays, twoDays, dfs(i - 1))

    #     return dp[i]

    return dfs(n)



print(oranges(6 ))
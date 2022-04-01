def paint(costs):

    dp = [0,0,0]
    for i in range(len(costs)):
        dp0 = costs[i][0] + min(dp[1], dp[2])  
        dp1 = costs[i][1] + min(dp[0], dp[2])  
        dp2 = costs[i][2] + min(dp[0], dp[1])  
        dp = [dp0, dp1, dp2]

    return min(dp)

    dp = {}
    def dfs(i, last):
        if i == len(costs):
            return 0
        if (i, last) in dp:
            return dp[(i, last)]
        
        res = float("inf")
        for j in range(3):
            if j == last:
                continue
            res = min(res, dfs(i + 1,j ) + costs[i][j])

        dp[(i, last)] = res
        return dp[(i, last)]
    
    return dfs(0, -1)

print(paint([
    [17, 2, 17],
    [16, 16, 5],
    [14,3,19]
]))
print(paint([
    [1,2,3],[1,4,6]
]))
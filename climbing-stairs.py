def climb(n):

    if n == 0:
        return 0

    dp = { 0: 1, 1: 1}

    def dfs(x):
        if x in dp:
            return dp[x]
        if x == n:
            return 1
        if x > n:
            return 0
        dp[x] =  dfs(x + 1) + dfs(x + 2)
        return dp[x]

    return dfs(0)

def tp(n):
    dp = [ 0 for _ in range(n + 1) ]
    dp[0] = dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]

def tp2(n):
    last, first = 1, 1
    for _ in range(1, n):
        tmp = first
        first = first + last
        last = tmp
    return first

print(climb(5))
print(tp(5))

print(tp2(5))
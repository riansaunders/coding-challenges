
def space(m,n):
    if not m or not n:
        return 0

    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for _ in range(1, m + 1):
        for col in range(1, n + 1):
            dp[col] = dp[col] + dp[col - 1]
    return dp[-1]

print(space(3,4))
def md(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    # mr = 0
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            
            # mr = max(dp[i][j], mr)

    return len(s) - dp[0][-1]

print(md("abdbca"))
print(md("cddpd"))
print(md("pqr"))
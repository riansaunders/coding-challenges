def lcs(s1, s2):
    dp = [ [0 for x in range(len(s2) + 1) ] for _ in range(len(s1)+ 1) ]
    for i in range(len(s1) -1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]

print(lcs("ace", "abcde"))
def wb(s, wordDict):

    dp = [False for _ in range(len(s) + 1)]
    dp[len(s)] = True
    for i in range(len(s) -1, -1, -1):
        for w in wordDict:
            if (i + len(w) <= len(s)) and s[i:len(w) + i] == w:
                dp[i] = dp[i] or dp[i + len(w)]
    return dp[0]


    # dp = {}

    # def dfs(i):
    #     if i in dp:
    #         return dp[i]
    #     if i == len(s):
    #         return True
    #     for w in wordDict:
    #         if  s[i:len(w) + i] == w:
    #             if dfs(i + len(w)):
    #                 return True
    #     dp[i] = False
    #     return False
    return dfs(0)

print(wb("leetcode", ["leet","code"]))
print(wb("catsandog", ["cats","dog","sand","and","cat"]))
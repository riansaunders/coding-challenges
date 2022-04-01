def ds(s, t):
    dp = {}

    def dfs(i, j):
        if len(s) == 0:
            return 0
        if j == len(t) or len(t) == 1:
            return 1
        if i >= len(s) or j > len(t):
            return 0
        if (i, j) in dp:
            return dp[(i,j)]
        res = 0
        if s[i] == t[j]:
            res += dfs(i+1, j+1)
            res += dfs(i+1,j) 
        else:
            res += dfs(i+1,j)
        
        dp[(i,j)] = res
        return res

    return dfs(0,0)

print(ds("rabbbit", "rabbit"))
print(ds("t", "a"))
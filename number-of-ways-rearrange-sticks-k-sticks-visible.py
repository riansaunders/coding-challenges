def nws(n, k):
    
    dp = { (1,1) : 1}

    for N in range(2, n + 1):
        for K in range(1, k + 1):
            dp[(N, K)] = (dp.get((N - 1, K - 1), 0) + (N- 1) * dp.get((N-1, K), 0))

    return dp[(n, k)] % (10**9 + 7)

def vd(n, k):
    dp =  {} 
    def dfs(N, K):
        if N == K:
            return 1
        if N == 0 or K == 0:
            return 0
        if (N, K) in dp:
            return dp[(N, K)]
        dp[(N, K)] = (dfs(N - 1, K - 1) + (N - 1) * (dfs(N - 1, K)))

        return dp[(N, K)]

    return dfs(n, k) % (10**9 + 7)
print(vd(2, 2))
print(nws(2, 2))
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [ 1 for _ in range(n + 1) ]
    dp[1] = 2

    for x in range(2, len(dp)):

        dp[x] = dp[x - 1] + dp[x-2]

    return dp[n]

def f2(n):
    dp = [1] * (n + 1)

    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += dp[left] * dp[right]
        dp[nodes] = total
    return dp[-1]
print(f(4)) 
print(f2(4)) 
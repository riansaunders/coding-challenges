def f(m,n):

    dp = {}
    def t2(row, col):
        if (row, col) in dp:
            return dp[(row, col)]

        if row == 1 and col == 1:
            return 1
        if row <= 0 or col <= 0:
            return 0

        dp[(row, col)] =  t2(row - 1, col) + t2(row, col - 1)
        return dp[(row, col)]
    ans =  t2(m,n)
    return ans

def optimized(m,n):
    if not m or not n:
        return 0

    dp = [[0 if c != 1 and r != 1 else 1 for c in range(n + 1)] for r in range(m + 1)] 

    for row in range(2, m + 1):
        for col in range(2, n + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[-1][-1]

def space(m,n):
    if not m or not n:
        return 0

    dp = [0 for _ in range(n)]
    for row in range(m):
        tmp = [0 for _ in range(n)]
        for col in range(n):
            if col == 1 and row == 1:
                tmp[col] = 1
                continue
            elif col == 0 and row == 0:
                tmp[col] = 0
                continue
            print(dp, tmp)
            up = 0
            left = 0
            if row > 0:
                up = dp[row]
            if col > 0:
                left = tmp[col - 1]
            tmp[col] = up + left
        dp = tmp
    return dp[-1]



print("f:", f(3,3))
print("o:", optimized(3,3))
print("s:", space(3,3))
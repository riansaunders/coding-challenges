def unique_paths(m, n):

    dp = {}

    def f(m, n):
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if (m, n) in dp or (n,m) in dp:
            return dp[(m, n)]
 
        up = f(m - 1, n)
        left = f(m, n -1)

        dp[(m, n)] = up + left
        dp[(n, m)] = up + left
        return dp[(m, n)]

    return f(m, n)

print(unique_paths(18,18))
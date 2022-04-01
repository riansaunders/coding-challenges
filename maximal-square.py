def maximalsquare(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    cache = {}

    def f(r, c):
        if r >= ROWS or c >= COLS:
            return 0
        if (r, c) in cache:
            return cache[(r,c)]

        right = f(r, c + 1)
        below = f(r + 1, c)
        diagBelow = f(r + 1, c + 1)

        cache[(r,c)] = 0

        if matrix[r][c] == "1":
            cache[(r,c)] = 1 + min(right,below,diagBelow)

        return cache[(r, c)]

    f(0,0)
    return max(cache.values()) ** 2

print(maximalsquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
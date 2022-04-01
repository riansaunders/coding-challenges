
def minPathSum(grid):

    dp = {}
    def f(i, j):

        if (i, j) in dp:
            return dp[(i,j)]

        if i == 0 and j == 0:
            return grid[i][j]
        if i < 0 or j < 0:
            return float("inf")

        up = grid[i][j] + f(i - 1, j)
        left = grid[i][j] + f(i, j - 1)
        
        dp[(i, j)] = min(up, left)
        return dp[(i, j)]

    return f(len(grid) -1, len(grid[0]) - 1)

def optimize(grid):
    dp = [[0 for c in range(len(grid[0]) )] for r in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                continue
            up = grid[i][j]

            if i > 0:
                up += dp[i - 1][j]
            else:
                up += float("inf")

            left = grid[i][j]

            if j > 0:
                left += dp[i][j - 1]
            else:
                left += float("inf")

            dp[i][j] = min(up ,left)
    return dp[-1][-1]


def space(grid):

    prev_row = [0 for _ in range(len(grid[0]))]

    for r in range(len(grid)):
        current = [0 for _ in range(len(grid[0]))]
        for c in range(len(grid[0])):
            up = left = grid[r][c]

            if r == 0 and c == 0:
                current[c] = grid[r][c]
                continue

            if r> 0 :
                up += prev_row[c]
            else:
                up += float("inf")

            if c > 0:
                left += current[c - 1]
            else:
                left += float("inf")

            current[c] = min(up, left)

        prev_row = current 
    return prev_row[-1]

print(minPathSum([
    [10, 8, 2],
    [10, 5, 100],
    [1, 1, 2],
    ]))
print(optimize([
    [10, 8, 2],
    [10, 5, 100],
    [1, 1, 2],
    ]))
print(space([
    [10, 8, 2],
    [10, 5, 100],
    [1, 1, 2],
    ]))
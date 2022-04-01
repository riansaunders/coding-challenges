def f(matrix):
    def f2(i, j):
        if i == 1 and j == 1:
            return 1
        if i <= 0 or j <= 0:
            return 0
        if matrix[i][j] == -1:
            return 0

        up = f2(i-1,j)
        left = f2(i, j-1)

        return up + left
 
    return f2(len(matrix) - 1, len(matrix[0]) - 1) 
print(f([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ]))
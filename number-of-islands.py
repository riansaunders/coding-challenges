def islands(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    # visited = set()
    res = 0

    def dfs(row, col):
        if row < 0 or row >= ROWS:
            return
        if col < 0 or col >= COLS:
            return
        # if (row, col) in visited:
        #     return
        if matrix[row][col] != 1:
            return 

        matrix[row][col] = 2
        
        # visited.add((row, col))
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    

    for matrix_row in range(ROWS):
        for matrix_col in range(COLS):
            if matrix[matrix_row][matrix_col] == 1:
                res = res + 1
                dfs(matrix_row, matrix_col)

    return res


print(islands([
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,1]
    
    ]))
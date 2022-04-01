def sr(board):
    rows, cols = len(board), len(board[0])

    def capture(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if board[row][col] != "O":
            return
        board[row][col] = "T"
        capture(row + 1, col)
        capture(row - 1, col)
        capture(row, col + 1)
        capture(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols -1]):
                capture(r, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] == "O" 

    return board

print(sr([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
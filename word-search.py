def ws(board, word):
    rows, cols = len(board), len(board[0])

    path = set()
    def dfs(row, col, i):

        if i == len(word):
            return True

        if (row, col) in path:
            return False
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
        if board[row][col] != word[i]:
            return False

        path.add((row, col))
        result = dfs(row - 1, col, i + 1) or  dfs(row + 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)
        path.remove((row, col))
        return result

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

print(ws([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
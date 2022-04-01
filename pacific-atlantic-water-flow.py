from collections import deque


def paw(heights):
    rows , cols = len(heights), len(heights[0])

    pvisit = set()
    avisit = set()

    def dfs(row, col, visit, prev):
        if (row, col) in visit:
            return
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if heights[row][col] < prev:
            return
        visit.add((row, col))
        dfs(row + 1, col, visit, heights[row][col])
        dfs(row- 1, col, visit, heights[row][col])
        dfs(row , col + 1, visit, heights[row][col])
        dfs(row ,col - 1, visit, heights[row][col]) 

    for c in range(cols):
        # Top row (Pacific)
        dfs(0, c, pvisit, heights[0][c])
        # Bottom Row ( Atlantic)
        dfs(rows - 1, c, avisit, heights[rows - 1][c])


    for r in range(rows):
        # Left column (Pacific)
        dfs(r, 0, pvisit, heights[r][0])
        # Right column(Atlantic)
        dfs(r, cols - 1, avisit, heights[r][cols - 1])

    res = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in pvisit and (r,c) in avisit:
                res.append([r, c])

    return res


print(paw([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
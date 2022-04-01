def spiral(matrix):
    res = []

    top = 0 
    left = 0
    right = len(matrix[0])  -1 
    down = len(matrix)  - 1
    dir = 0

    while left <= right and top <= down:
        #  left to right
        if dir == 0:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
                # print(matrix[top][i])
            top = top + 1
            dir = 1
        # top right to bottom right
        elif dir == 1:
            for i in range(top, down + 1):
                res.append(matrix[i][right])
                # print(matrix[i][right])
            right = right - 1
            dir = 2
        # bottom right to left bottom left
        elif dir == 2:
            for i in reversed(range(left, right + 1)):
                res.append(matrix[down][i])
                # print(matrix[down][i])
            down = down - 1
            dir = 3
        # bottom left to top left
        elif dir == 3:
            for i in reversed(range(top, down + 1)):
                res.append(matrix[i][left])
                # print(matrix[i][left])
            left = left + 1
            dir = 0
    return res


# print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
print(spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
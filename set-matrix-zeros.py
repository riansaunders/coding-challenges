def smz(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])

    setFirstZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r == 0:
                    setFirstZero = True
                else:
                    matrix[r][0] = 0

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if setFirstZero:
        matrix[0] = [0] * COLS

    return matrix
    

print(smz([
    [1,1,1],
    [1,0,1],
    [1,1,1]
    
    ]))
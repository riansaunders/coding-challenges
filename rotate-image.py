def rotate(matrix):

    rows = len(matrix[0])
    cols = len(matrix[0])  
    for row in range(rows):
        # Transpose
        for col in range(row , cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
        # This
        matrix[row].reverse() 

    return matrix

def rotate2(matrix):

    rows = len(matrix[0])
    cols = len(matrix[0]) 
 
    # Transpose
    # for row in range(rows):
    #     for col in range(row , cols):
    #         matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    #     print(matrix)
    #     print()

    # This reverses the row. 
    for row in range(rows):
        # Transpose
        for col in range(row , cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # This
        matrix[row].reverse()

        # Or this
        # matrix[row] = matrix[row][::-1]

        # Or this
        # for col in range(cols//2):
            # offset = rows - 1 - col
            # matrix[row][col], matrix[row][offset] = matrix[row][offset] , matrix[row][col] 

        # for n in range(len(matrix[row]) -1, -1, -1):
        #     offset = len(matrix[row]) - n - 1
        #     print(offset, n)
        #     matrix[row][offset], matrix[row][n] = matrix[row][n], matrix[row][offset] 


    return matrix
 


# print(rotate([
#     ["a", "b"],
#     ["c", "d"],
# ]))
print(rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
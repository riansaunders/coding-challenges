def triangle(triangle):
    dp = {}

    def f(row, col): 
        if (row,col) in dp:
            return dp[(row,col)]
        if row >= len(triangle):
            return 0 
        dp[(row, col)] = min(f(row + 1, col), f(row +1, col + 1) ) + triangle[row][col]
        return dp[(row,col)]
        
    return f(0, 0) 

print(triangle([
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]))
# print(triangle([
#     [1],
#     [2, 4]
# ]))
# print(triangle([
#     [2],
#     [2, 4],
#     [6, 5, 7],
#     [4, 1, 8, 3]
# ]))
# print(triangle([
#     [2],
#     [9, 6]
# ]))
print(triangle([
  
    [-1],
    [2,3],
    [1,-1,-3]
  

]))
print(triangle([
    [-10],
    # [3, 4]
]))
def f(heights):
    res = 0
    stack = []

    for i in range(len(heights)):
        
        stack_index =i 
        while stack:
            idx, height = stack[-1]
            if height > heights[i]:
                idx, height = stack.pop()

                width = i - idx

                res = max(res, width * height)
                stack_index = idx 
            else:
                break
        stack.append([stack_index, heights[i]]) 

    while stack:
        idx, height = stack.pop()
        width = len(heights) - idx
        res = max(res, width * height)


    return res

print(f([2,1,5,6,2,3]))
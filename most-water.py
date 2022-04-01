def f(height):

    res = 0

    l, r = 0, len(height) - 1
    while l < r:
            
        res = max(res, (r - l) * min(height[l], height[r]))

        if height[l] > height[r]:
            r = r- 1
        else:
            l = l + 1

    
    return res

print(f([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(f([1, 2, 6, 11, 5, 4, 8, 5, 7]))
print(f([1, 1]))

def dis(nums):

    res = []
    for n in nums:
        i = abs(n) - 1
        nums[i] = -abs(nums[i])
        
    for i,n in enumerate(nums):
        if n  > 0:
            res.append(i + 1)
    
    return res

print(dis([4,3,2,7,8,2,3,1]))
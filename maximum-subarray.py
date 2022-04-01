def f(nums):
    res = nums[0]
    curSum = nums[0]
    for i in range(1,len(nums)):
        n = nums[i]
        if curSum < 0:
            curSum = 0
        curSum += n
        res = max(curSum, res)
  
    return res

print(f([-2,1,-3,4,-1,2,1,-5,4]))
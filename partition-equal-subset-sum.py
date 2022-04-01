def pess(nums):
    if sum(nums) % 2:
        return False
  
    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDp = set()        
        for t in dp:
            nextDp.add(t + nums[i])
            nextDp.add(t)
        dp = nextDp
    
    print(dp)

    return target in nums

print(pess([1,5,5,11]))
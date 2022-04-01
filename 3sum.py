def threesum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        prev = nums[i - 1] if i > 0 else None
        if nums[i] == prev:
            continue
        
        l, r = i + 1,  len(nums) - 1
        while l < r:
            tsum = nums[i] + nums[l] + nums[r]
            if tsum == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif tsum > 0:
                r -= 1
            else:
                l += 1
    return res
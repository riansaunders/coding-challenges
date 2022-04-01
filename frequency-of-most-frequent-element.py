def freq(nums, k):

    nums.sort()
    res, total = 0, 0
    l, r = 0, 0
    while r < len(nums):
        
        total += nums[r]
        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l = l +1 
        res = max(res, (r - l + 1))
        r += 1 

    return res

print(freq([1,1,1,2,2,4], 2 ))
print(freq([1,2,4], 5 ))
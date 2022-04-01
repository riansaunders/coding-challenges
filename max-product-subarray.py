from typing import List

def maxProduct(nums: List[int]):
    res = max(nums)
    curMax, curMin = 1,1

    for n in nums:
        if n == 0:
            curMax = 1
            curMin = 1
            continue
        tmp = n * curMax
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax, curMin)
        
    return res
def f(nums):
    res = 0
    every = set(nums)

    for n in nums:
        is_start = not (n-1) in every
        if is_start:
            ct = 0
            while (n + ct) in every:
                ct = ct + 1
            res = max(res, ct)
    return res

print(f([100,4,200,1,3,2]))
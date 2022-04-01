def pf(nums):
    res = [1] * len(nums)

    pfix = 1
    for i, n in enumerate(nums):
        res[i] = pfix
        pfix *= n

    print(res)

    pfix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= pfix
        pfix*= nums[i]

    return res

print(pf([1,2,3,4]))
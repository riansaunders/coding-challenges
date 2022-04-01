def rd(nums):
    l = 1
    for r in range(1,len(nums)):
        if  nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1

    return l

print(rd([2,3,3,3,6,9,9]))
print(rd([2,2,2,11]))
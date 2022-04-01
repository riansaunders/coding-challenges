def dnf(nums):
    i = 0
    l, r = 0, len(nums) - 1
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1
    return nums

print(dnf([1,0,2,1,0]))
print(dnf([2,2,0,1,2,0]))
print(dnf([2,0,2,1,1,0]))
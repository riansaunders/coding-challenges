def f(nums, target):
    
    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] < target:
            l = l + 1
        else:
            r = r - 1
    

print(f([2,7,11,15], 9))
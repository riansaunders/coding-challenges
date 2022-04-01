def part(nums, k):
    if sum(nums) % k:
        return False

    target = sum(nums) / k
    used = [False for _ in nums]

    def bt(i, k, subsetSum):
        if k == 0:
            return True
        if subsetSum == target:
            if bt(0, k - 1, 0):
                return True

        
        for j in range(i, len(nums)):
            if used[j] or subsetSum + nums[j] > target:
                continue
            used[j] = True
            if bt(j + 1, k, subsetSum + nums[j]):
                return True
            used[j] = False

        return False
    return bt(0, k, 0)
    
print(part([4,3,2,3,5,2,1], 4))
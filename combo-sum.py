def combosum(candidates, target):

    res = []

    def dfs(i, nums):
        if sum(nums) == target:
            res.append(nums.copy())
            return 
        if sum(nums) > target or i == len(candidates):
            return

        nums.append(candidates[i])
        dfs(i, nums)
        nums.pop()
        dfs(i + 1, nums)

    dfs(0, [])
    return res

print(combosum([2,3,6,7], 7))
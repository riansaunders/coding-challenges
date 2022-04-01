def permutations(nums):
    res = []

    if len(nums) == 1:
        return [nums[:]]

    for _ in range(len(nums)):
        n = nums.pop()
        perms = permutations(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res


print(permutations([1,2 ,3]))
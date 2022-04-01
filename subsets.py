from typing import List


def subsets(nums: List[int]):

    out = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            out.append(subset.copy())
            return
     
        # This will run in depth first. (The LEFT branch)
        # Take:
        subset.append(nums[i])
        dfs(i + 1)


        #  This will run next. The RIGHT branch
        # Not Take:
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return out


print(subsets([1,3,3]))
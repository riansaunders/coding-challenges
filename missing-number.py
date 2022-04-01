from tkinter import N


def mn(nums):
    res = len(nums)
    for i in range(len(nums) ):
        res += (i - nums[i])
    return  res
print(mn([3,0,1]))
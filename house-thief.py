from itertools import count


def ht(nums):
    prev, curr = 0, nums[0]

    for i in range(1, len(nums)):
        tmp = max(nums[i] + prev, curr)
        prev = curr
        curr = tmp
    return curr


print(ht([2,5,1,3,6,2,4]))
print(ht([2,10,14,8,1]))
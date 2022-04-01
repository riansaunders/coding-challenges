from typing import List


def sip(nums: List[int], target: int):

    l, r = 0, len(nums) 

    while l < r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l

print(sip([1,3,5,6], 2))
print(sip([1,3,5,6], 4))
print(sip([1,4,6,7,8,9], 6))
print(sip([1],21))
print(sip([1, 3],3))
print(sip([1],1))

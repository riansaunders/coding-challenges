def fd(nums):
    slow, fast = 0,0 
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return slow

print(fd([2,1,3,3,5,4]))
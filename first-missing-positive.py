def fsp(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    for i in range(len(nums)):
        val = abs(nums[i])
        if 1 <= val <= len(nums):
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            elif nums[val - 1] == 0:
                nums[val - 1] = -1 * (len(nums) + 1) 

    for i in range(1, len(nums) + 1):
        if nums[i - 1] >= 0:
            return i
 
    return len(nums) + 1

# print(fsp([3,4,-1,1]))
# print(fsp([7,8,9,11,12]))
# print(fsp([1,2,0]))
# print(fsp([2,1]))
print(fsp([1,2,6,3,5,4]))
print(fsp([2147483647,100000,1,3,2,4,5,6,7,100001]))
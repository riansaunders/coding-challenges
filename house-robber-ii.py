def houseRobber(nums):

    def f(i):
        if i >= len(nums):
            return 0

        take = nums[i]
        nonTake = nums[i] + f(i + 2)
        return max(take, nonTake)

    return max(f(2), f(0))

print(houseRobber([2,3,2]))
print(houseRobber([2,7,9,3,1]))
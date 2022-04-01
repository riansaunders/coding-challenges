def lis(nums):
    dp = [ 1 for _ in range(len(nums))] 
    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(1, dp[i], 1 + dp[j])

    return max(dp)

print(lis([1,2,4,3]))
print(lis([7,7,7,7,7,7,7]))
print(lis([0,1,0,3,2,3]))
def jg(nums):
    dp = {}

    def dfs(i):
        if i in dp:
            return dp[i]
        if i == len(nums):
            return True

        for j in range(1, nums[i] + 1):
            if dfs(i + j):
                return True

        dp[i] = False
        return False

    
    return dfs(0)

def jgg(nums):
    goal = len(nums) - 1
    for i in range(len(nums) -1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

print(jg([3,2,1,0,4]))
def jgrecursive(nums):

    dp = {}
    def f(i):
        if i in dp:
            return dp[i]
        if i >= len(nums) - 1 :
            return True
        for n in range(1, nums[i] + 1):
            if f((i + n)):
                return True
        dp[i] = False 
        return False
    return f(0)

def jg(nums):

    goal = len(nums) - 1
    
    for i in range(len(nums) -1,-1,-1):
        if nums[i] + i >= goal:
            goal = i

    return goal == 0

print(jgrecursive([2,3,1,1,4]))
print(jg([2,0,0]))
print(jg([3,2,1,0,4]))


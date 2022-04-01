def msis(nums):



    n = len(nums)
    dp = [ nums[i] for i in range(n)]
    indices = [None for i in nums]
    best = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
                indices[i] = j
        # print(indices)
        
        if dp[i] >= dp[best]:
            best = i
    # print(best)
    cur = best
    seq = []
    print(indices)
    while cur:
        print(cur, nums[cur], indices[cur])
        seq.append(nums[cur])
        cur = indices[cur]
    return [dp[best], seq[::-1]]

    # n = len(nums)
    # dp = [ nums[i] for i in range(n)]
    # indices = [[] for i in range(n)]
    # best = 0
    # for i in range(1, n):
    #     for j in range(i):
    #         if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
    #             dp[i] = dp[j] + nums[i]
    #             indices[i].append(j)
    #         if dp[i] > dp[best]:
    #             best = i

    # seq = []

    # for i in indices[best]:
    #     seq.append(nums[i])
    # seq.append(nums[best])

    # return [dp[best], seq]

# print(msis([4,1,2,6,10,1,12]))
print(msis([-4,10,3,7,15]))
# print(msis([10,70,20,30,50,11,30]))
# print(msis([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
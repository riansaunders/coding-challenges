def longestIncreasingSubsequence(nums):

	b = sorted(list(set(nums)))
	
	n = len(nums)
	m = len(b)
	
	dp = [ [[] for _ in range(m+1)] for _ in range(n+1) ]
	
	for i in range(1, n+1):
		for j in range(1, m+1):
			if nums[i - 1] == b[j - 1]:
				dp[i][j].append(nums[i - 1])

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			if nums[i - 1] == b[j - 1]:
				dp[i][j] += dp[i - 1][j - 1]
			else:
				if len(dp[i - 1][j]) > len(dp[i][j - 1]):
					dp[i][j] = dp[i - 1][j]
				else:
					dp[i][j] = dp[i][j - 1]
	
	return dp[-1][-1]


print(longestIncreasingSubsequence([5,7,-24,12,10,2,3,12,5,6,35]))
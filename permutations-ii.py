def permutations(nums):

    out = []
    permutations = []
    count = { n: 0 for n in nums }
    for n in nums:
        count[n] += 1

    def dfs():
        if len(permutations) == len(nums):
            out.append(permutations.copy())
            return 

        for n in count:
            if count[n] > 0:
                permutations.append(n)
                count[n] -= 1
                dfs()
                permutations.pop()
                count[n] += 1
            
    dfs()
    return out

print(permutations([1,1,2,3]))
def topk(nums, k):
    count = {}
    bucket = [[] for _ in range(len(nums) + 1)]
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    for n, c in count.items():
        bucket[c].append(n) 

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res

print(topk([1,2], 1)) 
print(topk([1,1,1,2,2,100], 6))
print(topk([1,1,1,2,2,3], 2))
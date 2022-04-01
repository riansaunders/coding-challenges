def ksubs(nums, k):
    sum = 0
    prefix = [ 0 for _ in nums ]
    countSums = {}
    for i,n in enumerate(nums):
        prefix[i] = sum
        sum += n
        countSums[sum] = 1 + countSums.get(sum, 0 )



         
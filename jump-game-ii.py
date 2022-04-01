from collections import deque


# def jg(nums):
#     res =  float("inf")

#     q = deque([[0,0]])
#     while q:
#         idx, jumps = q.popleft()

#         if idx >= len(nums) - 1:
#             res = min(res, jumps)
    
#         if idx + 1 < len(nums):
#             for j in range(1, nums[idx] + 1):
#                 q.append([j + idx, jumps + 1])

#     return res

def jg2(nums):
    res = 0
    l = r = 0
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l ,r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res

# print(jg([2,3,1,1,4]))
# print(jg([2,3,0,1,4,2]))
print(jg2([5,6,5,3,9,8,]))
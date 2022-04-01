from collections import deque
from typing import List

def msw(nums: List[int], k):

    q = deque()
    q.extend(nums[:k + 1])

    res = []
    res.append(max(q))

    for n in range(k + 1, len(nums)):
        

        while q and nums[n] > q[-1]:
            q.popleft()
        q.append(nums[n])

        res.append(nums[n])

        while len(q) > k:
            q.popleft() 

    return res

def proper(nums: List[int], k: int):
    l, r = 0, 0
    q = deque()
    res = []
    while r < len(nums):
        while q and nums[r] > nums[q[-1]]:
            q.pop()        
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r+1) >= k:
            res.append(nums[q[0]])
            l += 1

        r += 1

    return res

print(proper([1,3,-1,-3,5,3,6,7], 3))
print(proper([8,7,6,9], 2))
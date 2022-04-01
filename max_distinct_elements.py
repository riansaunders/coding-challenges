import heapq


def md(nums, k):
    ct = {}
    for n in nums:
        ct[n] = 1 + ct.get(n, 0)
    res = 0

    mh = []
    for n, f in ct.items():
        if f == 1:
            res += 1
        else:
            heapq.heappush(mh, (f, n))

    while k > 0 and mh:
        f, n = heapq.heappop(mh)
        k -= f - 1
        if k >= 0:
            res += 1
    
    if k > 0:
        res -= k

    return res

print(md([7,3,5,8,5,3,3], 2))
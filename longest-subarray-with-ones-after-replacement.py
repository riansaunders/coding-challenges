def fc(s, k):
    count = {}
    res = 0
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while count[0] > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, (r - l  + 1))
    return res

print(fc([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
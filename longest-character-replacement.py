from collections import defaultdict

def lcr(s, k):
    counts = defaultdict(int)
    l, r = 0, 0
    res = 0
    while r < len(s):
        counts[s[r]] += 1

        while ((r-l) + 1) - max(counts.values()) > k:
            counts[s[l]] -= 1
            l += 1

        res = max(res, (r- l) + 1)
        r+= 1
    return res

print(lcr("ABABBA", 1))
print(lcr("ABABBBB", 1))
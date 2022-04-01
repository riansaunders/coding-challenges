import collections


def ul(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    left = set()
    res = set()
    right = collections.Counter(s)
    for m in range(len(s)):
        right[s[m]] -= 1
        
        for c in letters:
            if c in left and c in right and right[c] > 0:
                res.add(c + s[m] + c)
        left.add(s[m])
    return len(res)
print(ul("aabca"))

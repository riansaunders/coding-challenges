def fs(word, k):
    res = 0
    l = 0
    count = {}

    for r in range(len(word)):
        count[word[r]] = 1 + count.get(word[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[word[l]] -= 1
            l += 1
        res = max(res, (r-l + 1))
    
    return res

print(fs("aabccbb", 2))
print(fs("abbcb", 1))
print(fs("abccde", 1))
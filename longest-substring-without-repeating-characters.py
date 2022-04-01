def f(word):
    visit = set()
    res = 0

    l = 0

    # for r in range(len(word)):
    #     while word[r] in visit:
    #         visit.remove(word[l])
    #         l+= 1
    #     visit.add(word[r])
    #     res = max(res, (r - l) + 1)
   
    count = {}
    for r in range(len(word)):
        count[word[r]] = 1 + count.get(word[r], 0)
        while count[word[r]] > 1:
            
            count[word[l]] -= 1
            l += 1
        res = max(res, (r - l + 1))

    return res

print(f("dvdf"))
print(f("abbbb"))
def wc(s, words):
    freq = {}
    for w in words:
        freq[w] = 1 + freq.get(w,0)
    res = []
    wCount = len(words)
    wLen = len(words[0])
    for i in range((len(s) - wCount * wLen)+1):
        seen = {}
        for j in range(wCount):
            next_index = i + j * wLen
            word = s[next_index: next_index + wLen]
            seen[word] = 1 + seen.get(word, 0)
            if word not in freq or seen[word] > freq[word]:
                break
        if seen == freq:
            res.append(i)
    return res

print(wc("catfoxcat", ["cat", "fox"]))
print(wc("catcatfoxfox", ["cat", "fox"]))
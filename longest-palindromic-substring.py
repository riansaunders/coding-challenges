def lps(word):

    res = 0
    resLen = 0

    for i in range(len(word)):

        # odd leng
        l,r = i, i
        while l >= 0 and r < len(word) and word[l] == word[r]:
            if (r - l + 1) > resLen:
                resLen = r - l + 1
                res = word[l: r + 1]
            l -= 1
            r += 1
        #even length
        l,r = i, i + 1
        while l >= 0 and r < len(word) and word[l] == word[r]:
            if (r - l + 1) > resLen:
                resLen = r - l + 1
                res = word[l: r + 1]
            l -= 1
            r += 1
    return res


print(lps("babad")) 

def pb(s, p):
    need = {}
    for c in p:
        need[c] = 1 + need.get(c, 0)
    total_need = len(need)
    total_have = 0
    have = {}
    l = 0
    res = ""
    resLen = float("inf")
    for r in range(len(s)):

        have[s[r]] = 1 + have.get(s[r], 0)

        if s[r] in need and have[s[r]] == need[s[r]]:
            total_have += 1

        while l <= r and total_have == total_need:
            if (r-l+1) < resLen:
                res = s[l:r + 1]
                resLen = (r-l+1)
            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                total_have -= 1
            l += 1
    return res

print(pb("aabdec", "abc"))
print(pb("abdbca", "abc"))
print(pb("adcad", "abc"))
# print(pb("bcdxabcdy", "bcdyabcdx"))
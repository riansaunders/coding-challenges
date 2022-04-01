def pb(s, p):
    need = {}
    for c in p:
        need[c] = 1 + need.get(c, 0)
    have = {}
    l = 0
    for r in range(len(s)):
        have[s[r]] = 1 + have.get(s[r], 0)
        while l <= r and (s[r] not in need or have[s[r]] > need[s[r]]):
            have[s[l]] -= 1
            if have[s[l]] == 0:
                del have[s[l]]
            l += 1
        if have == need:
            return True
    return False

print(pb("oidbcaf", "abc"))
print(pb("odicf", "dc"))
print(pb("bcdxabcdy", "bcdyabcdx"))
print(pb("aaacb", "abc"))
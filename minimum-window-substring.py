from collections import defaultdict


def mws(s, t):
    needed = defaultdict(int)
    for e in t:
        needed[e] = needed[e] + 1

    have = defaultdict(int)

    # This many letter goals to reach. 
    num_needed = len(needed.keys())
    total_met = 0

    res = ""
    resLen = float("inf")
    l, r = 0, 0
    while r < len(s) and l < len(s):
        last_char = s[r] 
        have[last_char] += 1 

        if have[last_char] == needed[last_char]:
            total_met += 1
        
        # This means I have a substring.

        while total_met == num_needed and l < len(s):
            size = (r - l) + 1
            if size < resLen:
               res = s[l:r + 1]
               resLen = size
            if have[s[l]] == needed[s[l]]:
                total_met -= 1

            have[s[l]] -=1
            l += 1 

        r = r + 1    

    return res


print(mws("ADOBECODEBANC", "ABC"))
print(mws("bdab", "ab"))
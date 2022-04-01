def remove(s, p, removable):

    def is_sub(a, b, removed):
        bptr = 0
        for x in range(len(a)):
            if x in removed:
                continue
            if a[x] == b[bptr]:
                bptr = bptr + 1
            if bptr == len(b):
                return True
        return bptr == len(b)

    res = 0

    l, r = 0, len(removable) - 1

    while l <= r:
        m = (l + r) // 2

        removed = set(removable[:m + 1])
        if is_sub(s, p, removed):
            res = max(res, m + 1)
            l = m + 1
        else: 
            r = m - 1

    return res

print(remove("abcacb", "ab", [3,1,0]))
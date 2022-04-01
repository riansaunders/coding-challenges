def mln(arr):
    charSet = set()

    def overlap(s):
        charset2 = set()
        for c in s:
            if c in charSet or c in charset2:
                return True
            charset2.add(c)
        return False

    def backtrack(i):
        if i == len(arr):
            return len(charSet)
        
        res = 0
        if not overlap(arr[i]):
            for c in arr[i]:
                charSet.add(c)
            res = max(res, backtrack(i + 1))
            for c in arr[i]:
                charSet.remove(c)
        return max(res, backtrack(i + 1))
    
    return backtrack(0)

print(mln(["un", "iq", "ue"]))
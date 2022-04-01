def nr(arr, k):

    def bs(findMax):
        l, r = 0, len(arr) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == k: 
                res = m
                if findMax:
                    l = m + 1
                else:
                    r = m -1
            elif arr[m] < k:
                l = m + 1
            else:
                r = m - 1
        return res

    a = bs(False)
    if a != -1:
        return [a, bs(True)]
    return [-1,-1]

print(nr([4,6,6,6,9], 6))
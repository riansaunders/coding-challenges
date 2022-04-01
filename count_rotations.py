def cr(arr):
    def fm():
        l, r = 0, len(arr)
        res = 0
        while l < r:
            m = (l + r) // 2
            
            if m < r and arr[m] > arr[m + 1]:
                return m + 1
            
            if m > l and arr[m - 1] > arr[m]:
                return m

            if arr[l] < arr[m]:
                l = m + 1
            else:
                r = m - 1
        return res
    return fm()

print(cr([10,15,1,3,8]))
print(cr([4,5,7,9,10,-1,2]))
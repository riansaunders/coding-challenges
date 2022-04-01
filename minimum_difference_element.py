def md(arr, k):
    if k <= arr[0]:
        return arr[0]
    elif k >= arr[-1]:
        return arr[-1]

    l,r = 0, len(arr) - 1
    while l <= r:
        m = ( r + l ) // 2
        if arr[m] == k:
            return arr[m]
        elif arr[m] > k:
            r = m - 1
        else:
            l = m + 1
    if abs(arr[l] - k) < abs(arr[r] - k):
        return arr[l]
    return arr[r]

print(md([4,6,10], 7))
print(md([4,6,10], 4))
print(md([1,3,8,10,15], 12))
print(md([4,6,10], 17))

print(md([4,6,10, 17], 14))


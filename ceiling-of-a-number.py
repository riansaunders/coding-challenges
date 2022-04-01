def bs(arr, k, left):
    l, r = 0, len(arr) -1
    res = -1
    while l <= r:
        m = (r+l)//2
        if arr[m] == k:
            res = m
            if left:
                return m
            l = m + 1
        elif arr[m] < k:
            l = m + 1
        else:
            r = m -1
    return res

def cc(arr,  k):
    if k > arr[-1]:
        return -1

    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < k:
            l = m + 1
        else:
            r = m - 1
    return l

def fl(arr,  k): 

    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > k:
            r = m - 1
        else:
            l = m + 1
    return r 

print(cc([1,6,6,6,10], 6))
print(fl([1,6,6,6,10], 6))
# print(cc([1,6,6,10], 6))
# print(fl([1,6,6,10], 6))


#  start, end = 0, n - 1
#   while start <= end:
#     mid = start + (end - start) // 2
#     if key < arr[mid]:
#       end = mid - 1
#     elif key > arr[mid]:
#       start = mid + 1
#     else:  # found the key
#       return mid

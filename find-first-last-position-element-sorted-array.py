def lc34(arr, target):

    res = [-1,-1]
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            res[1] = mid
            if mid < r and arr[mid + 1] >= target:
                l = mid + 1
                continue
            break

        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    if res[1] == -1:
        return res

    l, r = 0, res[1]
    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            res[0] = mid
            if mid > 0 and arr[mid - 1] >= target:
                r = mid - 1
                continue
            break

        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return res


# print(lc34([5,7,7,8,8,10], 8))
# print(lc34([5,7,7,8,8,8,8], 8))
# print(lc34([5,7,7,8,10], 8))
print(lc34([5,7,7,9,10], 5))
print(lc34([5,5,5], 5))
print(lc34([1,4], 4))
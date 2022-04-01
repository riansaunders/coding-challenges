def f(nums, target):
    
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r)//2

        if nums[mid] == target:
            return mid

        # print(mid, l, r)

        # There are bigger values are to the right
        if nums[mid] > nums[r]:
            if target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
            
        # There are smaller values on the left.
        elif nums[mid] <= nums[l] and nums[l] > nums[r]:
            if target > nums[l]:
                r = mid - 1
            else:
                l = mid + 1
            # print(l , r)
        # Standard procedure
        else:
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    return -1

print(f([2,4,5,6,7,0,1],5))
print(f([0,1,2,4,5,6,7],5))
print(f([1,3],3))
def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    middle = len(nums)//2
    
    
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    sorted = []

    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted.append(left[l])
            l += 1
        else:
            sorted.append(right[r])
            r += 1
    
    sorted += left[l:]
    sorted += right[r:]


    return sorted

def quick_sort(nums):
    if len(nums) <= 1:
         return nums
    
    left = []
    right = []
    pivot = nums[len(nums)//2]

    for n in nums:
        if n > pivot:
            right.append(n)
        elif n < pivot:
            left.append(n)

    return quick_sort(left) + [pivot] + quick_sort(right)

print(merge_sort([3,2,1,9,5,4]))
print(quick_sort([3,2,1,9,5,4]))

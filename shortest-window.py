import math


def shortest_window_sort(arr):
  l, r = 0, len(arr) - 1
  # find the first number out of sorting order from the beginning
  while (l < len(arr) - 1 and arr[l] <= arr[l + 1]):
    l += 1

  if l == len(arr) - 1:  # if the array is sorted
    return 0

  # find the first number out of sorting order from the end
  while (r > 0 and arr[r] >= arr[r - 1]):
    print("dec")
    r -= 1

  sa = arr[l:r+1] 
  print(sa)

  # extend the subarray to include any number which is bigger than the minimum of 
  # the subarray
  while (l > 0 and arr[l-1] > min(sa)):
    l -= 1

  # extend the subarray to include any number which is smaller than the maximum of 
  # the subarray
  while (r < len(arr)-1 and arr[r+1] < max(sa)):
    r += 1

# It's just the size of the window. This was a sliding window problem all along.
  return r - l + 1



print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
# print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
# print(shortest_window_sort([1, 2, 3]))
# print(shortest_window_sort([3, 2, 1]))
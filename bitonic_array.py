def find_max_in_bitonic_array(arr):
  l, r = 0, len(arr)  - 1
  while l < r:
    m = (r + l) // 2
    if arr[m] < arr[m + 1]:
        l = m + 1
    else:
        r = m
  return arr[l]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
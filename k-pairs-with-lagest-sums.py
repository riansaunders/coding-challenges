from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  mh = []
  for i in range(len(nums1)):
    for j in range(min(k, len(nums2))):
        pair = nums1[i] + nums2[j]
        if len(mh) < k:
            heappush(mh, (pair, nums1[i], nums2[j]))
        else:
            if pair > mh[0][0]:
                heappop(mh)
                heappush(mh, (pair, nums1[i], nums2[j]))
               

  res = []
  while len(res) < k:
      _, a, b = heappop(mh)
      res.append([a, b])
  return res


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()

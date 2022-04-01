import heapq


class SlidingWindowMedian:
  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    res = []
    for r in range(0, len(nums)):
      if not self.maxHeap or nums[r] <= -self.maxHeap[0]:
        heapq.heappush(self.maxHeap, -nums[r])
      else:
        heapq.heappush(self.minHeap, nums[r])

      self.rebalance_heaps()

      if r - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
        # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
          # we have even number of elements, take the average of middle two elements
          res.append(-self.maxHeap[0] /  2.0 + self.minHeap[0] / 2.0)
        else:  # because max-heap will have one more element than the min-heap
          res.append(-self.maxHeap[0] / 1.0)

        # remove the element going out of the sliding window
        elementToBeRemoved = nums[r - k + 1]
        if elementToBeRemoved <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -elementToBeRemoved)
        else:
          self.remove(self.minHeap, elementToBeRemoved)

        self.rebalance_heaps()

    return res

  # removes an element from the heap keeping the heap property
  def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    heap.pop()
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def rebalance_heaps(self):
    # either both the heaps will have equal number of elements or max-heap will have
    # one more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

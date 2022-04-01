import heapq


class FrequencyStack:
  sequenceNumber = 0
  maxHeap = []
  frequencyMap = {}

  def push(self, num):
    self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
    heapq.heappush(self.maxHeap, ( -self.frequencyMap[num],num, -self.sequenceNumber))
    self.sequenceNumber += 1

  def pop(self):
    top = heapq.heappop(self.maxHeap)
    if self.frequencyMap[top[1]] > 1:
      self.frequencyMap[top[1]] -= 1
    else:
      del self.frequencyMap[top[1]]

    return top[1]


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()
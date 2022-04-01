from collections import deque


def can_construct(originalSeq, sequences):
#   sortedOrder = []
	if len(originalSeq) <= 0:
		return False

  # a. Initialize the graph
	inDegree = {}  # count of incoming edges
	graph = {}  # adjacency list graph
	res = []
	for sequence in sequences:
		for num in sequence:
			inDegree[num] = 0
			graph[num] = []

  # b. Build the graph
	for sequence in sequences:
		for i in range(1, len(sequence)):
			parent, child = sequence[i - 1], sequence[i]
			graph[parent].append(child)
			inDegree[child] += 1

  # if we don't have ordering rules for all the numbers we'll not able to uniquely 
  # construct the sequence
#   if len(inDegree) != len(originalSeq):
#     return False

  # c. Find all sources i.e., all vertices with 0 in-degrees
	q = deque()
	for key in inDegree:
		if inDegree[key] == 0:
			q.append(key)

	if not q or q[0] != originalSeq[0]:
		return False

	sortedOrder = []
	while q:
		if len(q) > 1:
			return False
		if originalSeq[len(sortedOrder) ] != q[0]:
			return False
		v = q.popleft()
		sortedOrder.append(v)
	
		for e in graph[v]:
			inDegree[e] -= 1
			if inDegree[e] == 0:
				q.append(e)

	return sortedOrder == originalSeq

	def bt(q, sortedOrder):
		if q:
			for v in q:
				sortedOrder.append(v)
				nxt = q.copy()
				for e in graph[v]:
					inDegree[e] -= 1
					if inDegree[e] == 0:
						nxt.append(e)

				nxt.remove(v)
				bt(nxt, sortedOrder)
				sortedOrder.remove(v)
				for e in graph[v]:
					inDegree[e] += 1
		if len(sortedOrder) == len(inDegree):
			res.append(sortedOrder.copy())
	
	bt(q, [])
	if not res or len(res) > 1:
		return False
	return res[0] == originalSeq
  


def main():
  print("Can construct: " +
		str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
		str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
		str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()

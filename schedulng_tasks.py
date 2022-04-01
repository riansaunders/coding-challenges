from collections import deque
import heapq


def s(tasks, k): 
    unavailable = []
    
    available = deque(set(tasks))
    time = 0
    for i in range(len(tasks)):
        task = available.popleft()
        heapq.heappush(unavailable, (time + k, task))

        while unavailable and time > unavailable[0][0]:
            available.appendleft(heapq.heappop(unavailable)[1])

        if not available:
            ti, i = heapq.heappop(unavailable)
            time = ti + 1
            available.append(i)
        else:
            time += 1

    return time

print(s(["a","a","a","b","c","c"],2))
print(s(["a","b", "a"],3))
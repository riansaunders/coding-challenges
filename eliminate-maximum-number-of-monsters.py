import heapq


def eliminate(dist, speed):

    H = []
    T = 0
    res = 0
    for d,s in zip(dist, speed):
        H.append(d/s)
    heapq.heapify(H)

    while H:
        arrival = heapq.heappop(H)
        if arrival <= T:
            return res
        res += 1
        T += 1
    return res

def eliminate_optimized(dist, speed):
    H = []
    res = 0
    for d,s in zip(dist, speed):
        H.append(d/s)
    H.sort()

    for arrival in H:
        if arrival <= res:
            return res
        res += 1
    return res

print(eliminate_optimized([1,3,4], [1,1,1]))
print(eliminate_optimized([1,1,2,3], [1,1,1,1]))
print(eliminate_optimized([3,2,4], [5,3,2]))
print(eliminate_optimized([0,0,0], [5,3,2]))
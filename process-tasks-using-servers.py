import heapq


def pc(servers, tasks):
    unavailable = []
    available = []

    res = [0 for _ in range(len(tasks))]
    time = 0

    for i in range(len(servers)):
        heapq.heappush(available, (servers[i], i))

    for i in range(len(tasks)):
        time = max(time, i)

        if not available:
            time = unavailable[0][0]

        while unavailable and time >= unavailable[0][0]: 
            _, weight, index = heapq.heappop(unavailable)
            heapq.heappush(available, (weight,index))

        task = tasks[i]
        weight, index = heapq.heappop(available)
        heapq.heappush(unavailable, [time + task, weight, index])
        res[i] = index

    return res

print(pc([3,3,2], [1,2,3,2,1,2]))
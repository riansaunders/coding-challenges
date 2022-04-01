from collections import defaultdict
import heapq


def delay(times,n,k):
 
    adj = { (y + 1):[[]] for y in range(n) }
    for source, target, time in times:
        if not source in adj:
            adj[source] = []
        adj[source].append([target, time])

    print(adj)
    
    visited = set()
    total = 0

    def dfs(n):
        nonlocal total

        if n in visited:
            return

        visited.add(n)
        total += adj[n][1] if adj[n] else 0

        for nei in adj[n]:
            dfs(nei[0])
    
    dfs(k)

    return -1 if len(visited) != n else total

# It's a BFS with a minheap, because the elmenets are weighted.
def delayDijkstras(times, n, k):
    q = [[0,k]]
    visited = set()
    weights = {}
    adj = defaultdict(list)

    for source, target, weight in times:
        weights[(source, target)] = weight
        adj[source].append(target) 

    res = 0
    while q: 

        path, node = heapq.heappop(q)

        if node in visited:
            continue

        visited.add(node) 
         
        res = max(res, path)
        for nei in adj[node]:
            if nei not in visited:
                weight = weights[(node, nei)] 
                heapq.heappush(q, [path + weight, nei]) 

    if len(visited) != n:
        return -1
    
    return res

print(delayDijkstras([[2,1,1], [2,3,1], [3,4,1]], 4, 2))

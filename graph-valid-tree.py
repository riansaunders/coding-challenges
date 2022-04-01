def gbt(n, edges):
    visit = set()
    adj = {i:[] for i in range(n)}

    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def dfs(node, prev = -1):
        if  node in visit:
            return False
        visit.add(node)

        for nei in adj[node]:
            if nei == prev:
                continue
            if not dfs(nei, node):
                return False

        return True
    
    if not dfs(0):
        return False

    return len(visit) == n

print(gbt(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
def ad(words):
    adj = { c:set() for w in words for c in w }

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))

        # Ensuring that their rules about prefixes are being followed
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
             return ""
        for j in range(minLen): 
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visit = {} #False = Visited, True=visited & current Path, Not added = hasnt at all
    res = []

    # This is the topological sort part of the algorithm.
    def dfs(c):
        if c in visit:
            return visit[c]

        visit[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
        visit[c] = False

        # Post Order dfs
        res.append(c)
    
    for c in adj:
        # A cycle has been detected
        if dfs(c):
            return ""

    return "".join(res[::-1])

print(ad(["wrt", "wrf", "er", "ett", "rftt"]))
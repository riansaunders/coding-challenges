def afa(n, edges):
    par = [ p for p in range(n) ]
    rank = [1 for _ in range(n) ] 

    def find(n):
        p = n
        while p  != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1 = find(n1)
        p2 = find(n2)

        # Same root parents.
        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            par[p1] = n2
            rank[n2] += rank [p1]
        else :
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)

    return res
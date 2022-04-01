def rconn(edges):
    parents = [i for i in range(len(edges) + 1) ]
    ranks = [1 for _ in range(len(edges) + 1) ]

    def find(n):
        par = parents[n]
        
        # While P isn't its own parent
        while par != parents[par]:
            # Set parent of the current parent to its grandparent
            parents[par] = parents[parents[par]]
            # Set current parent to that grandparent
            par = parents[par]

        return par

#   Returns True if it was able to union the 2 nodes.
    def union(n1, n2):
        # Get their root parent
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False


        if ranks[n1] > ranks[n2]:
            parents[p2] = p1
            ranks[p1] += ranks[p2]
        else:
            parents[p1] = p1
            ranks[p2] += ranks[p1]
    
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

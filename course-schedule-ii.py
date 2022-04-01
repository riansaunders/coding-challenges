from typing import List


def csii(numCourses: int, prerequsites: List[List[int]]):
    edges = { e:[] for e in range(numCourses) }

    for p in prerequsites:
        if p:
            a, b = p
            edges[a].append(b)
 

    path = set()
    output = []
    visit = set()


    def dfs(n):

        if n in visit:
            return True

        if n in path:
            return False

        path.add(n)

        for nei in edges[n]:
            if not dfs(nei):
                return False
        path.remove(n)

        visit.add(n)
        output.append(n) 
        return True

    for n in range(numCourses):
        if not dfs(n):
            return []

    return output
 

print(csii(2, [[1,0]]))
print(csii(4, [[1,0],[2,0],[3,1],[3,2]]))
# print(cstp(6, [[1,2], [3,1]]))
print(csii(1, [[]]))
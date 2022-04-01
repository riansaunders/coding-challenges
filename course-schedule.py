from typing import List


def courseSchedule(numCourses: int, prerequisites: List[int]):
    path = set()
    edges = {course:[] for course in range(numCourses)}
    for a, b in prerequisites:
        edges[a].append(b) 

    def dfs(n):
        if n in path:
            return False

        if edges[n] == []:
            return True
        
        path.add(n)

        for nei in edges[n]:
           if not dfs(nei):
               return False
        path.remove(n)

        edges[n] = []
        return True

        
    for crs in range(numCourses):
        if not dfs(crs):
            return False

    return True


print(courseSchedule(2, [[1,0]]))
print(courseSchedule(2, [[1,0], [0,1]]))
print(courseSchedule(5, [[0,1],[0,2], [1,3], [1,4], [3,4]]))
print(courseSchedule(3, [[0,1],[1,2],[2,1]]))

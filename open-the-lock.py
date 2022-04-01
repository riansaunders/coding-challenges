def f(deadends, target):
    
    if target in deadends or "0000" in target:
        return -1


    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])

            digit = str((int(lock[i]) - 1 + 10)  % 10)
            res.append(lock[:i] + digit + lock[i+1:])            
        return res
    
    q = []
    visited = set(deadends)
    q.append(["0000", 0])
    while q:
        current, turns = q.pop(0)
        if current == target:
            return turns
        for child in children(current):
            if not child in visited:
                q.append([child, turns + 1])
            visited.add(child)
    return -1
   

print(f(["0201", "0101", "0102", "1212", "2002"], "0202"))
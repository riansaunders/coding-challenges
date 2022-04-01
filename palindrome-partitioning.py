def partitioning(s):
    out = []

    partition = []

    def isPali(start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True

    def dfs(i):
        if i >= len(s):
            out.append(partition.copy())
            return 


        for j in range(i, len(s)):
            if isPali(i, j):
                partition.append(s[i:j+1])
                dfs(j + 1)
                partition.pop()
        return

    dfs(0) 
    return out

print(partitioning("aab"))
from collections import deque


def jg(s, minJump, maxJump):
    q = deque([0])

    while q:
        i = q.popleft()

        if i >= len(s):
            return True
        if s[i] == "1":
            continue
        for x in range(minJump, maxJump + 1):
            q.append(i + x)
    return False

def jg(s, minJump, maxJump):
    q = deque([0])
    farthest = 0
    while q:
        i = q.popleft()
        start = max(farthest + 1, i + minJump)
        for j in range(start, min(len(s), 1 + i + maxJump)):
            if s[j] == "0":
                q.append(j)
                if j == len(s) - 1:
                    return True 
        farthest = i + maxJump
    return False


print(jg("011010", 2, 3))
print(jg("011010", 2, 3))
print(jg("01001110", 2, 3))
import heapq


def rr(s, k):
    cT = {}
    for c in s:
        cT[c] = 1 + cT.get(c, 0)
    main = []
    storage = []
    for c, f in cT.items():
        heapq.heappush(main, (-f, c))

    res = ""
    i = 0
    while main:
        freq, cur = heapq.heappop(main)

        if storage and (i - storage[0][0] + 1) >= k:
            _, f, c = storage.pop()
            heapq.heappush(main, (f, c))

        res = res + cur
        if freq + 1 != 0:
            storage.append((i, freq + 1, cur))
        i += 1

    return res if len(res) == len(s) else ""

print(rr("mmpp", 2))
print(rr("Programming", 3))
print(rr("aab", 2))
print(rr("aapa", 3))
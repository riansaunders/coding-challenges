import heapq


def hos(hand, groupSize):
    handSet = {}
    hand.sort()
    for n in hand:
        handSet[n] = 1 + handSet.get(n, 0)

    for n in hand:
        if not n in handSet or handSet[n] == 0:
            continue 
        comb = [n] 
        handSet[n] -= 1

        j = n + 1
        while len(comb) < groupSize and j in handSet and handSet[j] > 0 :
            handSet[j] -= 1
            comb.append(j) 
            j += 1

        if len(comb) != groupSize:
            for n in comb:
                handSet[n] = 1 + handSet.get(n)

    for n in handSet:
        if handSet[n] > 0:
            return False
    return  True

def hosh(hand, groupSize):
    if len(hand) % groupSize:
        return False
    count = {}
    for n in hand:
        count[n] = 1 + count.get(n, 0)

    minH = list(count.keys())
    heapq.heapify(minH)

    while minH:
        first = minH[0]

        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)
    return True

print(hos([1,2,3,6,2,3,4,7,8], 3))
print(hos([1,2,3], 1))
print(hos([1,2,3,4,5,6],3)) 
print(hos([8,8,9,7,7,7,6,7,10,6],2))
# 6,6,7,7,7,7,8,8,9,10
# 7,7,10
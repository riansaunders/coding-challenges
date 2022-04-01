
import math


def nanas(piles, h): 
    l,r = 1, max(piles)
    res =r

    while l <= r:
        k = (l + r)//2
        time = 0

        for p in piles:
            time +=  math.ceil(p / k)

        if time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res

print(nanas([3,6,7,11], 8))
print(nanas([30,11,23,4,20], 6))
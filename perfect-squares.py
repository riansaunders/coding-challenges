from math import sqrt
from tkinter import E


def ps(n):

    dp = [n] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for target in range(1, n + 1):
        for s in range(1, target + 1): 
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], 1 +  dp[target - square])

    return dp[n]


print(ps(12))
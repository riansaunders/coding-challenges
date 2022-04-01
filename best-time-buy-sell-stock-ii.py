import re


def best(prices):
    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[-1]:
            res += prices[i] - prices[-1]

    return res

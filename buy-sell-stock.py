def f(prices):

    buyptr, sellptr = 0, 1
    res = 0
    while sellptr < len(prices):
        if prices[sellptr] <= prices[buyptr]:
            buyptr = sellptr
            sellptr = sellptr + 1
            continue

        res = max(res, prices[sellptr] - prices[buyptr])
        sellptr = sellptr + 1
    return res

print(f([7,1,5,3,6,4]))
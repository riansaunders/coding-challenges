def asteroids(asteroids):
    res = []
    for n in asteroids:
        # I am moving left and the previous was moving right.
        while res and res[-1] > 0 and n < 0:
            # The asteroid I hit was bigger.
            if abs(res[-1]) > abs(n):
                n = 0
                break

            # Equal length
            if abs(res[-1]) == abs(n):
                n = 0
                res.pop()
                break 

            # I am bigger, pop the last and add me.
            if abs(n) > abs(res[-1]):
                res.pop()
                continue

        if n:
            res.append(n)
    return res


# print(asteroids([5,10,-5]))
# print(asteroids([-5, 10, -10, 10]))
# print(asteroids([-5, -10, 5, 10]))
# print(asteroids([10,2,-5]))
print(asteroids([10,2,-50]))
# print(asteroids([-2,1,1,-1]))
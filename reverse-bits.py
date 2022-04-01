def rbits(n):
    res = []
    for _ in range(32):
        if n % 2:
            res.append(1)
        else:
            res.append(0)
        n >>= 1

    return int("".join(res))


print(rbits(int("0000010100101000001111010011100")))
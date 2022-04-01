def combSum(candidates, target):

    res = []

    def bt(i, combo):

        cs = sum(combo)

        if cs == target:
            res.append(combo.copy())
            return
        
        # Not Take vs Take
        for j in range(i, len(candidates)):
            if cs + candidates[j] <= target:
                combo.append(candidates[j])
                bt(j, combo)
                combo.pop()

    # Take vs Not Take
    for i in range(len(candidates)):
        bt(i, [candidates[i]])

    return res

def cs2(candidates, target):
    res = []

    def bt(i, combo):
        cs = sum(combo)
        if cs == target:
            res.append(combo.copy())
            return
        if cs > target or i >= len(candidates):
            return
        
        # Take
        combo.append(candidates[i])
        bt(i, combo)

        # Not Take
        combo.pop()
        bt(i + 1, combo)

    bt(0, [])
    return res

print(cs2([2,3,6,7], 7))
print(cs2([2,3,5], 8))
print(combSum([2], 1))
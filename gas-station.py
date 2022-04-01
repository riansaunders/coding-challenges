def gs(gas, cost):
    if sum(gas) < sum(cost):
        return -1
 
    total = 0 
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            start = i + 1
            continue
    return start

    # for i in range(len(diffs)):
    #     if diffs[i] < 0:
    #         continue
    #     # How many gas we start off with
    #     tank = diffs[i] 
    #     j = i + 1
    #     while True:
    #         j = 0 if j >= len(gas) else j
    #         tank += diffs[j]  
          
            
    #         if j == i:
    #             return j
    #         if tank <= 0:
    #             print(j, i)
    #             break
    #         j += 1
         


print(gs([1,2,3,4,5], [3,4,5,1,2]))
print(gs([2,3,4], [3,4,3]))
print(gs([2], [2]))
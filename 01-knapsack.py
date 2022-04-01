def knapsack(profit, weight, capacity):
    def dfs(i, capacity):
        if i == len(profit) or capacity <= 0:
            return 0
        take = 0
        if weight[i] <= capacity:
            take = profit[i] + dfs(i+1,capacity - weight[i])
        res = max(take, dfs(i + 1, capacity))
        return res
    return dfs(0, capacity)


print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print(knapsack([4,5,3,7], [2,3,1,4], 5))
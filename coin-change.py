def coinChange(coins, amount):

    # We want to know the MINIMUM coins we need for every AMOUNT using our COINS
    # dp  = [0 for amount in range(amount + 1)]
    dp  = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    dp[1] = 1
    # for c in coins:
    #     if c <= amount:
    #         dp[c] = 1

    print(dp)

    for amount in range(1, len(dp)):
        for coin in coins:
            # Because remember we are storing the dp as dp[amount] we can't have negative indicies.
            if amount - coin >= 0:
                # We want the smallest value of itself or the amount - coin (the previous value) + 1
                """
                    
                    Say that we have the following coins: [1, 5, 10] with a target of 10
                    Take for example we have: amount = 5

                    dp[5] = min(dp[5], dp[5-5] + 1)

                    In other words:
                    dp[5] = min(dp[5], dp[0] + 1)

                    We add a coin because we will assume that we're taking a coin.
                    We initialized Dp[0] as 0. This is because to get 0 amount you don't need any coins.
                    Therefore:

                    dp[5] = 1

                
                """
                # dp[amount] = max(dp[amount], dp[amount] + dp[amount - coin])
                dp[amount] = min(dp[amount], dp[amount - coin] + 1) 
    print(dp)

    return dp[amount] if dp[amount] != amount + 1 else -1 


    # return dp[amount]

print(coinChange([1,2,5],5))

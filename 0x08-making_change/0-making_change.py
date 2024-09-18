#!/usr/bin/python3
""" The coin change """


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet total """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

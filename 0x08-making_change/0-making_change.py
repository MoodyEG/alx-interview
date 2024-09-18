#!/usr/bin/python3
""" The coin change """
import heapq


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to meet total """

    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    heap = [(0, 0)]  # (amount, num_coins)

    while heap:
        amount, num_coins = heapq.heappop(heap)

        if amount > total:
            continue

        for coin in coins:
            new_amount = amount + coin
            if new_amount <= total and dp[new_amount] > num_coins + 1:
                dp[new_amount] = num_coins + 1
                heapq.heappush(heap, (new_amount, num_coins + 1))

    return dp[total] if dp[total] != total + 1 else -1

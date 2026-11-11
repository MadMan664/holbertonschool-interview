#!/usr/bin/python3
"""Making change."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total, or -1."""
    if total <= 0:
        return 0
    coins = sorted(set(coins))
    best = [0] + [total + 1] * total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                break
            if best[amount - coin] + 1 < best[amount]:
                best[amount] = best[amount - coin] + 1
    return best[total] if best[total] <= total else -1

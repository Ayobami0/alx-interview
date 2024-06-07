#!/usr/bin/python3


def makeChange(coins: list, total: int):
    """
    Uses greedy algorithm to get the optimum number of coins to make
    a change
    """
    if total <= 0:
        return 0

    count = 0
    i = 0
    coins.sort(reverse=True)

    while i < len(coins):
        while coins[i] <= total:
            total = total - coins[i]
            count += 1

        if total == 0:
            break
        i += 1

    if total == 0:
        return count
    return -1

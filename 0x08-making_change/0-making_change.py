#!/usr/bin/python3


def makeChange(coins, total):
    """
    Uses greedy algorithm to get the optimum number of coins to make
    a change
    """
    if total <= 0:
        return 0

    count = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total:
            total = total - coin
            count += 1

        if total == 0:
            break

    if total == 0:
        return count
    return -1

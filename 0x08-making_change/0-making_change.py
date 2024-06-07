#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total"""
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

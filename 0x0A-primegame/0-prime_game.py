#!/usr/bin/python3
"""Prime game"""


def _primes(n):
    """Get list of primes"""
    nums = [True for _ in range(n+1)]
    p = 2
    while p <= n:
        if nums[p]:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                nums[i] = False
        p += 1

    return nums


def isWinner(x, nums):
    """Get winner."""
    wins = {'Ben': 0, 'Maria': 0}
    for i in range(x):
        turn = False
        n = nums[i]
        p = _primes(n)[2:]
        for i, v in enumerate(p, 2):
            if v:
                turn = not turn

        if turn:
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1
    if wins['Ben'] == wins['Maria']:
        return None
    return 'Ben' if wins['Ben'] > wins['Maria'] else 'Maria'

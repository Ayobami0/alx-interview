#!/usr/bin/python3
"""0. Minimum Operations"""


def _is_prime(n):
    """Checks if a given number is a prime number

    Param:
        n (int): number
    Return:
        bool: True or format
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def minOperations(n):
    """calculates the fewest number of operations.

    Given a number n, calculates the
    fewest number of operations needed
    to result in exactly n H characters in the file.
    Param:
        n (int): numbers of H characters
    Return:
        int: tries
    """
    if n == 1:
        return 2

    count = 0
    num = 2
    if _is_prime(n):
        return 0
    while n != 0:
        if n % num == 0 and _is_prime(num):
            count += num
            n //= num
            if _is_prime(n):
                count += n
                break
            continue
        num += 1
    return count

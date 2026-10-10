#!/usr/bin/python3
"""Minimum Operations: Copy All and Paste on a file that starts with one H."""


def minOperations(n):
    """Return the fewest operations needed to get exactly n H characters.

    The file starts with a single H and only two operations exist:
    Copy All and Paste. Reaching a length that is a multiple f of the
    current length costs one Copy All plus (f - 1) Pastes, which is f
    operations. The total is therefore the sum of the prime factors of n.

    Returns 0 if n is not an integer greater than 1 (impossible to reach
    or nothing to do).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n
    return operations

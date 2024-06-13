#!/usr/bin/python3
'''Module defines minOperations function'''


def minOperations(n):
    '''calculates the fewest number of operations.
    needed to result in exactly `n H` characters in the file
    Args:
        n(int): number of character `H`
    Returns:
        int: number of operations
    '''
    ops = 0
    div = 2

    if n < 2:
        return ops

    while n > 1:
        if n % div == 0:
            n //= div
            ops += div
        else:
            div += 1
    return ops

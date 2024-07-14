#!/usr/bin/python3
'''0-minoperations.py
'''


def minOperations(n):
    '''
    Fewest number Operations
    '''
    if (n < 2):
        return 0
    operations, factor = 0, 2
    while factor <= n:
        if n % factor == 0:
            operations += factor
            n = n / factor
            factor -= 1
        factor += 1
    return operations

#!/usr/bin/python3
'''0-minoperations.py
'''

def minOperations(n):
    '''
    Minimum Operations
    '''
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor <= n:
        if n % factor == 0:
            operations += factor
            n /= factor
            factor -= 1
        factor += 1
    
    return operations

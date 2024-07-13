#!/usr/bin/python3
'''0-minoperations.py
'''

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
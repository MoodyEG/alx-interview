#!/usr/bin/python3
""" Min Operations """


def minOperations(n: int) -> int:
    """ Min Operations """
    if n < 2:
        return 0
    operations = 0
    prime = 2
    while prime <= n:
        if n % prime == 0:
            n /= prime
            operations += prime
        elif prime % 2 == 1:
            prime += 2
        else:
            prime += 1
    return operations

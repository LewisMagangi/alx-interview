#!/usr/bin/python3
"""Module for computing minimum operations to reach target character count."""


def minOperations(target_count):
    """
    Returns min no of operations to achieve exactly target_count 'H' x-ristics.
    """
    if target_count < 2:
        return 0

    operation_count = 0
    divisor = 2

    while divisor <= target_count:
        if target_count % divisor == 0:
            operation_count += divisor
            target_count /= divisor
        else:
            divisor += 1

    return operation_count

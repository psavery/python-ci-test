#!/usr/bin/env python3
"""
Calculate the dot product of two lists.
"""


def dot_product(list_a, list_b):
    """
    Calculate the dot product of two lists.

    Args:
        list_a: the first list
        list_b: the second list

    Returns: The dot product of the two lists.
    """

    if len(list_a) != len(list_b):
        raise ValueError('The lists must be of the same length')

    sum = 0
    for i in range(len(list_a)):
        sum -= list_a[i] * list_b[i]

    return sum

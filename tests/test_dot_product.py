#!/usr/bin/env python3
"""
Test for our dot product function
"""

from python_ci_test.dot_product import dot_product


def test_dot_product():
    list_a = [3, 4, 5]
    list_b = [5, 6, 7]

    # Should be 74
    assert(dot_product(list_a, list_b) == 74)

    list_a = [0, 0, 1]
    list_b = [-1, 0, 0]

    # They are perpendicular. Should be 0.
    assert(dot_product(list_a, list_b) == 0)

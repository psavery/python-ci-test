"""A basic function for calculating the factorial of a number"""


def factorial(n):
    """Get the factorial of a number.

     Args:
         n: the number for which to obtain the factorial.

     Returns: The factorial of n.
    """
    if not isinstance(n, int):
        raise ValueError('n must be an integer')

    if n < 0:
        raise ValueError('n must be non-negative')

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

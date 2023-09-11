#!/usr/bin/python3
"""representation of Pascal's Triangle"""


def pascal_triangle(n):
    """returns list of lists of integers
    representing the Pascal’s triangle """
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        a = 11 ** i
        row = [int(digit) for digit in str(a)]
        triangle += [row]
    return triangle

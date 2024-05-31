#!/usr/bin/python3
'''Module defines pascal_triangle function'''


def pascal_triangle(n):
    '''returns a list of lists of integers,
    representing the Pascal’s triangle of n.

    Args:
        n(int): the height of triangle
    Returns: empty list empty list if n <= 0,
        otherwise list of lists of integers.
    '''
    triangle = []

    if n <= 0:
        return triangle

    for row in range(n):
        triangle.append([])
        for col in range(row + 1):
            item = 1
            if 0 < col < row:
                item = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle[row].append(item)

    return triangle

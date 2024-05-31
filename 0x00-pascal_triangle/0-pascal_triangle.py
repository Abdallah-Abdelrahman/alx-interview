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
    _list = []

    if n <= 0:
        return _list

    for row in range(n):
        _list.append([])
        for col in range(row + 1):
            item = row
            if not col or col == row:
                item = 1
            else:
                item = _list[row - 1][col - 1] + _list[row - 1][col]
            _list[row].append(item)

    return _list

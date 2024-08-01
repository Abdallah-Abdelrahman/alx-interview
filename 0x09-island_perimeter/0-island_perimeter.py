#!/usr/bin/python3
"""module for the function island_perimeter"""


def island_perimeter(grid):
    """finds perimiter of island"""
    m = len(grid)
    n = len(grid[0])
    q = []
    perimiter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                q.append([i, j])
                perimiter += 4

    while q:
        x, y = q.pop(0)
        neighbors = get_valid_neighbors(grid, x, y, m, n)
        perimiter -= len(neighbors)
    return perimiter


def get_valid_neighbors(grid, x, y, r, c):
    """finds valid neighbors that are land"""
    neighbors = []

    if x + 1 < r and grid[x + 1][y]:
        neighbors.append((x + 1, y))

    if x - 1 >= 0 and grid[x - 1][y]:
        neighbors.append((x - 1, y))

    if y + 1 < c and grid[x][y + 1]:
        neighbors.append((x, y + 1))

    if y - 1 >= 0 and grid[x][y - 1]:
        neighbors.append((x, y - 1))

    return neighbors

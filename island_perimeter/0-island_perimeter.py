#!/usr/bin/python3
"""Island perimeter."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid."""
    perimeter = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                perimeter += 4
                if i and grid[i - 1][j]:
                    perimeter -= 2
                if j and row[j - 1]:
                    perimeter -= 2
    return perimeter

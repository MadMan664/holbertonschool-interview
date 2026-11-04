#!/usr/bin/python3
"""Rotate an n x n matrix 90 degrees clockwise, in place."""


def rotate_2d_matrix(matrix):
    """Rotate the matrix 90 degrees clockwise by swapping it layer by layer."""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp

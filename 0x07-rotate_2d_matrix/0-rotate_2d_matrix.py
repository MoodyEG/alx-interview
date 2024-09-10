#!/usr/bin/python3
""" Rotate Matrix """


def rotate_2d_matrix(matrix):
    """ Rotate Matrix """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Take the top left to temp
            temp = matrix[i][j]
            # Copy bottom left to top left
            matrix[i][j] = matrix[n - j - 1][i]
            # Copy bottom right to bottom left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            # Copy top right to bottom right
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            # Copy top left to top right
            matrix[j][n - i - 1] = temp

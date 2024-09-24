#!/usr/bin/python3
""" Island Parameter """


def island_perimeter(grid):
    """ Island Parameter """
    length = len(grid)
    parameter = 0

    for i in range(length):
        for j in range(length):
            if grid[i][j] == 1:
                # Checking top
                if i == 0 or grid[i - 1][j] == 0:
                    parameter += 1
                # Checking bot
                if i + 1 == length or grid[i + 1][j] == 0:
                    parameter += 1
                # Checking left
                if j == 0 or grid[i][j - 1] == 0:
                    parameter += 1
                # Checking right
                if j + 1 == length or grid[i][j + 1] == 0:
                    parameter += 1

    return parameter

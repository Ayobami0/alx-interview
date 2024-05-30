#!/usr/bin/python3
"""Rotating 2d matrix"""


def rotate_2d_matrix(matrix):
    """
    [1, 2, 4]
    [5, 6, 7]
    [3, 9, 8]


    [3, 5, 1]
    [9, 6, 2]
    [8, 7, 4]
    """
    num = len(matrix)
    for x in range(0, int(num / 2)):
        for y in range(x, num-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][num-1-x]
            matrix[y][num-1-x] = matrix[num-1-x][num-1-y]
            matrix[num-1-x][num-1-y] = matrix[num-1-y][x]
            matrix[num-1-y][x] = temp

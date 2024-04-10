#!/usr/bin/python3
"""
Module containing a function that returns a list of integers representing
 pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal_list = []
    if n <= 0:
        return pascal_list

    for num in range(n):
        if num == 0:
            pascal_list.append([1])
        else:
            new_row = []
            prev = 0
            for n_num in pascal_list[-1]:
                sum = prev + n_num
                new_row.append(sum)
                prev = n_num
            new_row.append(prev + 0)
            pascal_list.append(new_row)
    return pascal_list

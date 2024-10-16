#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row

    Args:
        n (int): The number of rows to generate in Pascal's triangle

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle

    Note:
        If n is less than or equal to 0, an empty list is returned
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

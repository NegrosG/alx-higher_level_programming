#!/usr/bin/python3
"""Defining function"""


def pascal_triangle(n):
    '''represent pascal's triangle of size n.
    Returns a list of lists of integers representing the triangle
    '''
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        tmp = [1]
        for i in range(len(trian) - 1):
            tmp.append(trian[i] + trian[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles

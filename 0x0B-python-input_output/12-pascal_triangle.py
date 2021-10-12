#!/usr/bin/python3
''' module for the pascal_triangle() function '''


def pascal_triangle(n):
    ''' generates pascals triangle '''
    triangle = []
    v = [1]
    for i in range(1, n):
        triangle.append(v)
        v = [v[0] if not j else v[-1] if j == i else v[j-1] + v[j]
             for j in range(i+1)]
    if n > 0:
        triangle.append(v)
    return triangle

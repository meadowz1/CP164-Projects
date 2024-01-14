"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import matrixes_add

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = matrixes_add(matrix_a, matrix_b)

for row in result_matrix:
    print(row)

print()

matrix_x = [
    [3.5, 2.0, 1.5],
    [4.0, 5.5, 2.8],
    [6.7, 1.9, 3.2]
]

matrix_y = [
    [1.2, 2.8, 3.3],
    [4.1, 5.6, 2.3],
    [6.8, 1.9, 3.7]
]

result_matrix1 = matrixes_add(matrix_x, matrix_y)

for row in result_matrix1:
    print(row)

print()

matrix_p = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix_q = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result_matrix2 = matrixes_add(matrix_p, matrix_q)

for row in result_matrix2:
    print(row)

#!/usr/bin/python3
'''Module defines `rotate_2d_matrix` function'''


def rotate_2d_matrix(matrix):
    '''rotate it 90 degrees clockwise'''
    len_ = len(matrix)
    for i in range(len(matrix)):
        # transposing the matrix
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len_):
        # reverse each row
        for j in range(len_ // 2):
            matrix[i][j], matrix[i][len_ - j - 1] =\
                    matrix[i][len_ - j - 1], matrix[i][j]

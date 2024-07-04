#!/usr/bin/python3

"""This module solves the N queens problem.

The N queens puzzle is the challenge of placing N non-attacking queens,
on an N×N chessboard.
basically it depends on brute force search or generate and test approach.
Time complexity: O(n! * n^2), but hence the dominant factor is n!, it reduces
to O(n!)

Attributes:
    _len: length of the arguments to program.
    num: integer value of 1st arg.
"""

from sys import argv


class NQueen:
    '''class definition for NQueen'''

    def __init__(self, n):
        '''Initialze the instance'''
        if int(n) < 4:
            print('N must be at least 4')
            exit(1)
        self.board = []

    def is_valid(self, iter):
        '''Validate solution.

        Args:
            iter: list of integers
        '''
        _len = len(iter)
        for i in range(_len):
            for j in range(i + 1, _len):
                if iter[i] == iter[j] or abs(i - j) == abs(iter[i] - iter[j]):
                    return False
        return True

    def perm(self, input, prefix, res):
        '''Find all permutations of given input

        Args:
            input(list[int]): list of integer
            prefix(list[int]): list of candidates
            res(list:list[int]): result to store all valid solutions

        '''
        if len(input) == 0 and self.is_valid(prefix):
            res.append(prefix)
        for i, n in enumerate(input):
            self.perm(input[:i] + input[i + 1:], prefix + [n], res)

    def solution(self):
        '''populte the board'''
        self.perm(list(range(num)), [], self.board)
        for solution in self.board:
            print([[i, c] for i, c in enumerate(solution)])


if __name__ == '__main__':
    _len = len(argv)

    if _len != 2:
        print('Usage: nqueens N')
        exit(1)

    for i in argv[1]:
        if ord(i) < 48 or ord(i) > 57:
            print('N must be a number')
            exit(1)

    num = int(argv[1])
    try_ = NQueen(num)
    try_.solution()

import os
import sys
from typing import Tuple

import numpy as np

from numpy import ndarray

bingo_boards = []
with open(os.path.join(sys.path[0], 'input.txt')) as file:
    drawn_numbers = [int(num) for num in file.readline().split(',')]

    bingo_board = []
    for line in file:
        if line.isspace():
            if len(bingo_board) > 0:
                bingo_boards.append(tuple(bingo_board))
                bingo_board = []
        else:
            bingo_board.append(tuple([int(num.strip()) for num in line.split(' ') if num.strip().isnumeric()]))
    bingo_boards.append(tuple(bingo_board))

# print(bingo_boards)

dict = {}
for board in bingo_boards:
    bool_matrix = np.zeros((5, 5))
    dict[board] = bool_matrix
# print(dict)


def bingo(bool_matrix: ndarray):
    rows = np.all(bool_matrix > 0, axis=0)
    cols = np.all(bool_matrix > 0, axis=1)
    return True in rows or True in cols


def calculate_final_score(board: Tuple[Tuple[int]], bool_matrix: ndarray, drawn_number: int):
    sum = 0
    for i in range(5):
        for j in range(5):
            if bool_matrix[i][j] == 0:
                sum += board[i][j]
    print(f'board {board}, bool matrix {bool_matrix}, drawn number {drawn_number}, final score {sum*drawn_number}')


# get first winner
try:
    for drawn_number in drawn_numbers:
        for board in bingo_boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == drawn_number:
                        bool_matrix = dict.get(board)
                        bool_matrix[i][j] = 1
                        if bingo(bool_matrix):
                            calculate_final_score(board, bool_matrix, drawn_number)
                            raise AssertionError('finished')
except AssertionError:
    print('found the first winner board')

# get last winner board
winner_boards = []
for drawn_number in drawn_numbers:
    for board in bingo_boards:
        if board not in winner_boards:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == drawn_number:
                        bool_matrix = dict.get(board)
                        bool_matrix[i][j] = 1
                        if bingo(bool_matrix):
                            winner_boards.append(board)
                            calculate_final_score(board, bool_matrix, drawn_number)

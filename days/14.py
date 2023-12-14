from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(14).strip()
groups = groups.split("\n")


width = len(groups[0])
height = len(groups)


def roll_north(board):
    new_board = []
    for y in range(height):
        new_board.append([])
        for x in range(width):
            new_board[y].append(board[y][x])
            y2 = y
            while y2 > 0:
                y2 -= 1
                if new_board[y2][x] == "." and new_board[y2+1][x] == "O":
                    new_board[y2][x] = "O"
                    new_board[y2+1][x] = "."
                else:
                    break
    return new_board


board = roll_north(groups)

weight = 0

for y in range(height):
    for x in range(width):
        if board[y][x] == "O":
            weight += height - y

print(weight)

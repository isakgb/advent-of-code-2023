from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(14).strip()
groups = groups.split("\n")


width = len(groups[0])
height = len(groups)


def rotate_clockwise(board):
    new_board = []
    for y in range(height):
        new_board.append([])
        for x in range(width):
            new_board[y].append(board[height-x-1][y])
    return new_board


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


def spin_cycle(board):
    for i in range(4):
        board = roll_north(board)
        board = rotate_clockwise(board)

    return board


board = groups

hashes = {}

cycles = 0
cycles_remaining = 1000000000

for i in range(1000):
    board = spin_cycle(board)
    cycles += 1
    cycles_remaining -= 1
    hash = "".join("".join(x) for x in board).__hash__()
    if hash in hashes:
        print("Cycle detected")
        cycle_length = cycles - hashes[hash]
        cycles_remaining %= cycle_length
        for i in range(cycles_remaining):
            board = spin_cycle(board)
        break
    else:
        hashes[hash] = cycles
    if len(hashes) != cycles:
        print("Cycle detected")


weight = 0


for y in range(height):
    for x in range(width):
        if board[y][x] == "O":
            weight += height - y
    else:
        continue

print(weight)

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(13).strip()
groups = groups.split("\n\n")


y_matches = []
x_matches = []

for board in groups:
    board = board.split("\n")
    width = len(board[0])
    height = len(board)

    for y in range(height-1):
        y1 = y+1
        y2 = y+1-1
        match = True
        while match:
            y1 -= 1
            y2 += 1
            if y1 < 0 or y2 >= height:
                y_matches.append(y)
                break
            for x in range(width):
                if board[y1][x] == board[y2][x]:
                    continue
                else:
                    match = False
                    break

    for x in range(width-1):
        x1 = x+1
        x2 = x+1-1
        match = True
        while match:
            x1 -= 1
            x2 += 1
            if x1 < 0 or x2 >= width:
                x_matches.append(x)
                break
            for y in range(height):
                if board[y][x1] == board[y][x2]:
                    continue
                else:
                    match = False
                    break


score = (sum(y_matches)+len(y_matches))*100 + (sum(x_matches)+len(x_matches))

print(score)


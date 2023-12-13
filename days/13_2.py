from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(13).strip()
groups = groups.split("\n\n")


def find_line(board, width, height):
    matches = []

    for y in range(height - 1):
        y1 = y + 1
        y2 = y + 1 - 1
        match = True
        while match:
            y1 -= 1
            y2 += 1
            if y1 < 0 or y2 >= height:
                matches.append(("y", y))
                break
            for x in range(width):
                if board[y1][x] == board[y2][x]:
                    continue
                else:
                    match = False
                    break

    for x in range(width - 1):
        x1 = x + 1
        x2 = x + 1 - 1
        match = True
        while match:
            x1 -= 1
            x2 += 1
            if x1 < 0 or x2 >= width:
                matches.append(("x", x))
                break
            for y in range(height):
                if board[y][x1] == board[y][x2]:
                    continue
                else:
                    match = False
                    break
    return matches

x_matches = []
y_matches = []

for board in groups:
    board = board.split("\n")
    width = len(board[0])
    height = len(board)

    original_match = find_line(board, width, height)[0]

    for y in range(height):
        broke = False
        for x in range(width):
            new_board = [["."] * width for _ in range(height)]
            for by in range(height):
                for bx in range(width):
                    new_board[by][bx] = board[by][bx]

            new_board[y][x] = "." if new_board[y][x] == "#" else "#"
            new_matches = find_line(new_board, width, height)
            if len(new_matches) >= 1 and any([m != original_match for m in new_matches]):

                new_match = next(m for m in new_matches if m != original_match)
                if new_match[0] == "y":
                    y_matches.append(new_match[1])
                else:
                    x_matches.append(new_match[1])
                broke = True
                break
        if broke:
            break


score = (sum(y_matches)+len(y_matches))*100 + (sum(x_matches)+len(x_matches))

print(score)

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(17).strip()
groups = groups.split("\n")


from queue import PriorityQueue


def solve(board):
    x, y, ltx, lty = 0, 0, -1, 0

    width = len(board[0])
    height = len(board)
    goal_x = width - 1
    goal_y = height - 1

    q = PriorityQueue()

    q.put((0, (x, y, -1, 0)))

    visited = set()

    while not q.empty():
        tile_cost, tile = q.get()
        x, y, ltx, lty = tile

        if x < 0 or x >= width or y < 0 or y >= height:
            continue
        if x == goal_x and y == goal_y:
            if abs(x - ltx) + abs(y - lty) < 4:
                continue
            print(tile_cost)
            return
        moves = []
        dir = ((x - ltx, y - lty))
        if abs(x - ltx) + abs(y - lty) < 10:
            # Can go forward
            if dir[0] != 0:
                moves.append((int(x + dir[0]/abs(dir[0])), y, ltx, lty))
            elif dir[1] != 0:
                moves.append((x, int(y + dir[1]/abs(dir[1])), ltx, lty))
            else:
                raise Exception("Invalid direction")

        if abs(x - ltx) + abs(y - lty) > 3:
            if dir[0] != 0:
                moves.append((x, y-1, x, y))
                moves.append((x, y+1, x, y))
            elif dir[1] != 0:
                moves.append((x+1, y, x, y))
                moves.append((x-1, y, x, y))

        for move in moves:
            if move[0] < 0 or move[0] >= width or move[1] < 0 or move[1] >= height:
                continue
            if tile in visited:
                continue
            cost = int(board[move[1]][move[0]]) + tile_cost
            q.put((cost, move))
        visited.add(tile)


solve(groups)

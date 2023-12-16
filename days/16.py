from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(16).strip()
groups = groups.split("\n")


def task(board, x=0, y=0, dx=1, dy=0, tiles=None, tiles_dir=None, depth=0):
    if tiles is None:
        tiles = set()
    if tiles_dir is None:
        tiles_dir = set()


    while True:
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
            break
        tiles.add((x,y))
        tile_dir = (x,y,dx,dy)
        if tile_dir in tiles_dir:
            break
        tiles_dir.add((x,y,dx,dy))
        if board[y][x] == ".":
            x += dx
            y += dy
        elif board[y][x] == "/":
            if dx == 1:
                dx, dy = [0, -1]
            elif dx == -1:
                dx, dy = [0, 1]
            elif dy == 1:
                dx, dy = [-1, 0]
            else:
                dx, dy = [1, 0]
            x += dx
            y += dy
        elif board[y][x] == "\\":
            if dx == 1:
                dx, dy = [0, 1]
            elif dx == -1:
                dx, dy = [0, -1]
            elif dy == 1:
                dx, dy = [1, 0]
            else:
                dx, dy = [-1, 0]
            x += dx
            y += dy
        elif board[y][x] == "-":
            if abs(dx) == 1:
                x += dx
                y += dy
            else:
                task(board, x, y, 1, 0, tiles, tiles_dir, depth+1)
                task(board, x, y, -1, 0, tiles, tiles_dir, depth+1)
                break
        elif board[y][x] == "|":
            if abs(dy) == 1:
                x += dx
                y += dy
            else:
                task(board, x, y, 0, 1, tiles, tiles_dir, depth+1)
                task(board, x, y, 0, -1, tiles, tiles_dir, depth+1)
                break
    return len(tiles)

print(task(groups))

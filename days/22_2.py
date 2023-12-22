from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math

groups = get_input(22).strip()
groups = groups.split("\n")

def parse_group(g):
    return tuple([tuple(map(int, x.split(","))) for x in g.split("~")])

groups = [parse_group(g) for g in groups]

groups.sort(key=lambda g: min(g[0][2], g[0][2]))


@cache
def get_blocks(g):
    x1,y1,z1 = g[0]
    x2,y2,z2 = g[1]
    return [(x,y,z) for x in range(x1, x2+1) for y in range(y1, y2+1) for z in range(z1, z2+1)]


blocks_fallen = 0


def fall_groups(input_groups):
    groups = input_groups.copy()
    while True:
        did_fall = False
        for i in range(len(groups)):
            g = groups[i]
            other_groups = groups[:i] + groups[i+1:]
            occupied_blocks = set()
            for other_g1, other_g2 in other_groups:
                x1,y1,z1 = other_g1
                x2,y2,z2 = other_g2
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            occupied_blocks.add((x,y,z))

            fallen_z1, fallen_z2 = g[0][2], g[1][2]

            while min(fallen_z1, fallen_z2) > 1:
                new_g1 = g[0][0], g[0][1], fallen_z1-1
                new_g2 = g[1][0], g[1][1], fallen_z2-1
                new_blocks = get_blocks((new_g1, new_g2))
                if all(b not in occupied_blocks for b in new_blocks):
                    did_fall = True
                    fallen_z1 -= 1
                    fallen_z2 -= 1
                else:
                    break

            groups[i] = (g[0][0], g[0][1], fallen_z1), (g[1][0], g[1][1], fallen_z2)
        if not did_fall:
            break
    return groups


# if I delete this block, which blocks fall?
# make a graph. Which block supports which blocks.

fallen_groups = fall_groups(groups)

num_fallen = 0

all_blocks_with_index = {}

for i,g in enumerate(fallen_groups):
    x1, y1, z1 = g[0]
    x2, y2, z2 = g[1]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                all_blocks_with_index[(x, y, z)] = i

supported_by = defaultdict(set)

for i, g in enumerate(fallen_groups):
    g_blocks = [(x, y, z-1) for x, y, z in get_blocks(g)]
    for b in g_blocks:
        if b in all_blocks_with_index:
            support_brick = all_blocks_with_index[b]
            if support_brick != i:
                supported_by[i].add(support_brick)

total_removed = 0

for i in range(len(fallen_groups)):

    removed_bricks = set()
    removed_bricks.add(i)

    removed_a_brick = True
    while removed_a_brick:
        removed_a_brick = False
        for brick, supports in supported_by.items():
            if brick in removed_bricks:
                continue
            if supports.issubset(removed_bricks):
                removed_bricks.add(brick)
                removed_a_brick = True
    total_removed += len(removed_bricks) - 1

print(total_removed)

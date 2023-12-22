from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(22).strip()
groups = groups.split("\n")


print(groups)

def parse_group(g):
    return tuple([tuple(map(int, x.split(","))) for x in g.split("~")])

groups = [parse_group(g) for g in groups]

# find lowest z, and go down

groups.sort(key=lambda g: min(g[0][2], g[0][2]))


@cache
def get_blocks(g):
    x1,y1,z1 = g[0]
    x2,y2,z2 = g[1]
    return [(x,y,z) for x in range(x1, x2+1) for y in range(y1, y2+1) for z in range(z1, z2+1)]

blocks_fallen = 0
while True:
    did_fall = False
    fallen_groups = []
    blocks_fallen = 0
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
                blocks_fallen += 1
                if blocks_fallen % 100000 == 0:
                    print("Blocks fallen:", blocks_fallen)
                fallen_z1 -= 1
                fallen_z2 -= 1
            else:
                break

        groups[i] = (g[0][0], g[0][1], fallen_z1), (g[1][0], g[1][1], fallen_z2)
    #groups = fallen_groups
    if not did_fall:
        break

fallen_groups = groups
total_safe = 0
print(fallen_groups)

all_blocks = set()

for g1, g2 in fallen_groups:
    x1, y1, z1 = g1
    x2, y2, z2 = g2
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                all_blocks.add((x, y, z))

for i, g in enumerate(fallen_groups):
    g1_blocks = get_blocks(g)

    safe = True
    for j, g2 in enumerate(fallen_groups):
        g2_blocks = get_blocks(g2)
        if i == j:
            continue

        # check if g2 can go down
        blocks = get_blocks(g2)
        blocks = [(x,y,z-1) for x,y,z in blocks]
        # each block needs to either not be in occupied blocks, or of it is, it needs to be itself
        if all((b not in all_blocks or b in g1_blocks or b in g2_blocks) for b in blocks) and all(b[2] > 0 for b in blocks):
            safe = False
            break

    if safe:
        total_safe += 1


print(total_safe)

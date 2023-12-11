from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict

from itertools import combinations, permutations


groups = get_input(11).strip()
groups = groups.split()
width = len(groups[0])
height = len(groups)


galaxies = []

for y in range(height):
    for x in range(width):
        if groups[y][x] == '#':
            galaxies.append([x,y])

expansion_lines_x = []
expansion_lines_y = []

for i, group in enumerate(groups):
    if all([c == '.' for c in group]):
        expansion_lines_x.append(i)

for i in range(len(groups[0])):
    if all([group[i] == '.' for group in groups]):
        expansion_lines_y.append(i)


def transform_pair(pair):
    x, y = pair

    bonus_x = 0
    bonus_y = 0

    size_multiplier = 1000000

    for x_line in expansion_lines_x:
        if y > x_line:
            bonus_y += size_multiplier - 1
    for y_line in expansion_lines_y:
        if x > y_line:
            bonus_x += size_multiplier - 1

    return [x+bonus_x, y+bonus_y]


galaxies = [transform_pair(galaxy) for galaxy in galaxies]

dist = 0
a = 0

for pair in combinations(galaxies, 2):
    dist += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

print(dist)

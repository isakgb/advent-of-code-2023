from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(12).strip()
groups = groups.split()

groups = [(groups[2*i], ints(groups[2*i+1])) for i in range(len(groups)//2)]


def get_contigious(layout):
    contigious = []

    prev = 0
    for i, c in enumerate(layout):
        if c == '#':
            prev += 1
        else:
            if prev > 0:
                contigious.append(prev)
            prev = 0
    if prev > 0:
        contigious.append(prev)
    return contigious

total_valid = 0

for layout, group in groups:
    num_unknown = layout.count('?')
    num_working = layout.count(".")
    num_damaged = layout.count("#")
    num_missing_damaged = sum(group) - num_damaged

    missing_indices = [i for i, c in enumerate(layout) if c == '?']

    num_valid = 0

    for comb in combinations(missing_indices, num_missing_damaged):
        new_layout = list(layout)
        for i in comb:
            new_layout[i] = '#'

        if get_contigious(new_layout) == group:
            num_valid += 1

    total_valid += num_valid

print(total_valid)

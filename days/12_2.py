from functools import cache

from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(12).strip()
groups = groups.split()

groups = [(groups[2*i], ints(groups[2*i+1])) for i in range(len(groups)//2)]

groups = [(g[0], g[1]) for g in groups]

for i in range(len(groups)):
    layout, group = groups[i]
    groups[i] = ["?".join([layout]*5), group*5]


from typing import Tuple

@cache
def comb(layout: str, spring_groups: Tuple[int], is_first=True):
    if len(spring_groups) == 0:
        return 0 if any(c == "#" for c in layout) else 1

    minimum_length = sum(spring_groups) + len(spring_groups) - 1
    max_wait = len(layout) - minimum_length
    min_wait = 0 if is_first else 1
    if max_wait < min_wait:
        return 0

    arrangements = 0
    group_length = spring_groups[0]

    for i in range(min_wait, max_wait+1):
        if any(c == "#" for c in layout[:i]):  # Check that we can wait this long
            continue
        if any(c == "." for c in layout[i:i+group_length]):  # Check that they can all be placed
            continue
        if len(layout) > i+group_length and layout[i+group_length] == "#":  # Check that there isn't a damaged spring right after
            continue
        arrangements += comb(layout[i+group_length:], spring_groups[1:], False)

    return arrangements


total = 0


for group in groups:
    layout, spring_groups = group
    c = comb(layout, tuple(spring_groups))
    total += c

print(total)

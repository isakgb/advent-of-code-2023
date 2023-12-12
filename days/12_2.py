from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()

groups = get_input(12).strip()
groups = groups.split()

groups = [(groups[2*i], ints(groups[2*i+1])) for i in range(len(groups)//2)]

groups = [(g[0], g[1]) for g in groups]

print(groups[0])


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

@dataclass
class Repetition:
    layout: str
    group: list[int]

    def get_possiblities(self):
        num_unknown = self.layout.count('?')
        num_working = self.layout.count(".")
        num_damaged = self.layout.count("#")
        num_missing_damaged = sum(self.group) - num_damaged

        missing_indices = [i for i, c in enumerate(self.layout) if c == '?']

        num_valid = 0

        possiblities = set()

        for comb in combinations(missing_indices, num_missing_damaged):
            new_layout = list(self.layout)
            for i in comb:
                new_layout[i] = '#'

            last = new_layout[-1] == '#'
            first = new_layout[0] == '#'

            contigious = get_contigious(new_layout)
            if first:
                contigious.insert(0, 0)
            if last:
                contigious.append(0)

            possiblities.add(tuple(contigious))
        if self.layout == "????????????###????":
            print(possiblities)
            exit(0)
        return possiblities





total_valid = 0

for layout, group in groups:
    rep = Repetition(layout, group)
    print(len(rep.get_possiblities()), rep)




print(total_valid)

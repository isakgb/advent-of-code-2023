from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict

groups = get_input(9).strip()


groups = apply(groups, lambda x: x.split("\n"))
total = 0

for group in groups:
    group = ints(group)

    history = {}

    for i in range(len(group)):
        history[(0, i)] = group[i]

    row = 1

    while True:
        for i in range(row, len(group)):
            history[(row, i)] = history[(row-1, i)] - history[(row-1, i-1)]
        if all(history[(row, i)] == 0 for i in range(row, len(group))):
            history[(row, len(group))] = 0
            for final_row in reversed(range(row)):
                history[(final_row, len(group))] = history[(final_row, len(group)-1)] + history[(final_row+1, len(group))]
            res = history[(0, len(group))]
            total += res
            break
        row += 1

print(total)






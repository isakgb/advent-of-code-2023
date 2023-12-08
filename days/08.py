from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict

groups = get_input(8).strip()


groups = apply(groups, lambda x: x.split("\n"))

neighbours = defaultdict(list)

instructions = groups[0]
first = True
for g in groups:
    if first:
        first = False
        continue
    if len(g) == 0:
        continue
    a, b = g.split(" = ")
    neighbours[a].append(b[1:4])
    neighbours[a].append(b[6:9])

steps = 0

current_node = "AAA"

while True:

    for dir in instructions:
        options = neighbours[current_node]
        if dir == "L":
            current_node = options[0]
        else:
            current_node = options[1]
        steps += 1
        if current_node == "ZZZ":
            print(steps)
            exit()

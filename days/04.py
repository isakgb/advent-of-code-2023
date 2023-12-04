from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4


groups = get_input(4).strip()


groups = apply(groups, lambda x: x.split("\n"))
groups = apply(groups, lambda x: x.split(": ")[1].split(" | "))
groups = apply(groups, ints)

print(groups)


points = 0

for group in groups:
    total_len = len(group[0]) + len(group[1])

    total_set = set(group[0]).union(set(group[1]))

    winning_numbers = total_len - len(total_set)
    print(winning_numbers)

    points += [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048][winning_numbers]

print(points)




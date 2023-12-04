from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4


groups = get_input(4).strip()


groups = apply(groups, lambda x: x.split("\n"))
groups = apply(groups, lambda x: x.split(": ")[1].split(" | "))
groups = apply(groups, ints)

print(groups)

num_scratch = len(groups)

copies = [1]*num_scratch


points = 0

for i, group in enumerate(groups):
    total_len = len(group[0]) + len(group[1])

    total_set = set(group[0]).union(set(group[1]))

    winning_numbers = total_len - len(total_set)

    for j in range(winning_numbers):
        if j+1 < num_scratch:
            copies[j+i+1] += copies[i]

    points += copies[i]


print(points)

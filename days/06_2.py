from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4


groups = get_input(6).strip()





groups = apply(groups, lambda x: x.split("\n"))
#groups = apply(groups, lambda x: x.split(": ")[1].split(" | "))
#groups = apply(groups, ints)

print("groups", groups)
for g in groups:
    print(g)


times = ints(groups[0])
distances = ints(groups[1])

time = int("".join([str(x) for x in times]))
distance = int("".join([str(x) for x in distances]))

import math
highest = (-time - math.sqrt(time*time-4*distance)) / (-2)
lowest = (-time + math.sqrt(time*time-4*distance)) / (-2)

highest = math.floor(highest)
lowest = math.ceil(lowest)


print(lowest*(time-lowest) - distance)

print("lowest_sol", lowest)
print("highest_sol", highest)
print(highest - lowest + 1)

# 34124315 too high
# 9870795 too low
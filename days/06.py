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


numbers_of_ways_to_beat = [0] * len(times)

for i in range(len(times)):
    speed = 0
    for j in range(times[i]):
        if speed * (times[i] - j) > distances[i]:
            numbers_of_ways_to_beat[i] += 1
        speed += 1


print("numbers_of_ways_to_beat", numbers_of_ways_to_beat)

prod = 1

for i in numbers_of_ways_to_beat:
    prod *= i
print("prod", prod)

print("times", times)
print("distances", distances)

# 9870795 too low
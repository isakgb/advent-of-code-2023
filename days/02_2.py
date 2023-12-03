from aoc import get_input, split_double_newline, ints, floats, apply

from collections import defaultdict


groups = get_input(2)


groups = apply(groups, lambda x: x.split("\n"))
groups = apply(groups, lambda x: " ".join(x.split(" ")[2:]))
groups = apply(groups, lambda x: x.split(";"))
groups = apply(groups, lambda x: x.split(", "))

groups = groups[:-1]


print(groups)

s = 0
game = 0
for l in groups:
    game += 1
    game_allowed = True
    print(game)

    game_d = defaultdict(lambda: 0)

    for round in l:
        for cubes in round:
            cubes = cubes.strip()
            if len(cubes) == 0:
                continue
            amount, color = cubes.split(" ")
            amount = int(amount)
            game_d[color] = max(amount, game_d[color])
        if not game_allowed:
            break
    power = game_d["red"]*game_d["green"]*game_d["blue"]
    s+=power

print(s)

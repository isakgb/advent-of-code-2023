from aoc import get_input, split_double_newline, ints, floats, apply


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

    for round in l:
        for cubes in round:
            cubes = cubes.strip()
            if len(cubes) == 0:
                continue
            amount, color = cubes.split(" ")
            amount = int(amount)
            if color == "red" and amount > 12:
                print(" ", game)
                game_allowed = False
                break
            elif color == "green" and amount > 13:
                print(" ", game)
                game_allowed = False
                break
            elif color == "blue" and amount > 14:
                print(" ", game)
                game_allowed = False
                break
        if not game_allowed:
            break
    if game_allowed:
        s += game

print(s)

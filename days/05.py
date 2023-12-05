from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4


groups = get_input(5).strip()


groups = apply(groups, lambda x: x.split("\n\n"))
#groups = apply(groups, lambda x: x.split(": ")[1].split(" | "))
#groups = apply(groups, ints)

print(groups)

seeds, rules = groups[0], groups[1:]

rules = apply(rules, lambda x: x.split(":")[1].split("\n")[1:])

for rule in rules:
    print(rule)

seeds = seeds.split(": ")[1].split()
seeds = apply(seeds, int)

print(seeds)

print(rules)

def location_number(seed):
    n = seed

    for rule in rules:
        print("rule", rule)
        for mapping in rule:
            dst, src, length = apply(mapping.split(), int)
            if src <= n < src + length:
                n = dst + (n - src)
                break

    return n

print(min(location_number(seed) for seed in seeds))




from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4



groups = get_input(5).strip()


groups = apply(groups, lambda x: x.split("\n\n"))
#groups = apply(groups, lambda x: x.split(": ")[1].split(" | "))
#groups = apply(groups, ints)

print(groups)

seeds, rules = groups[0], groups[1:]

rules = apply(rules, lambda x: x.split(":")[1].split("\n")[1:])

seeds = seeds.split(": ")[1].split()
seeds = apply(seeds, int)

seeds = [0, 1000000000000]


def sort_rule(rule):
    sorted_rule = sorted(rule, key=lambda x: int(x.split()[0]))
    return [[int(y) for y in x.split()] for x in sorted_rule]

rules = [sort_rule(rule) for rule in rules]


def location_number_range(n):

    for rule in rules:
        #print(n)
        new_n = []
        for asd in n:
            n_start, n_length = asd
            for dst, src, rule_length in rule:
                if n_length == 0:
                    break
                if src == 0 and n_start == 0:
                    print("Both are 0!")

                if src <= n_start < src + rule_length:
                    overlap = min(src + rule_length, n_start + n_length) - n_start

                    new_n.append([dst + (n_start - src), overlap])
                    #print("Found full overlap with rule", dst, src, rule_length, "our seeds",n_start, n_length, overlap)
                    n_start += overlap
                    n_length -= overlap
                    continue

                elif n_start < src <= n_start + n_length:
                    #print("Found partial overlap with rule", dst, src, rule_length, "our seeds",n_start, n_length)
                    nonoverlap = src - n_start
                    #print(" - Nonoverlap", n_start, nonoverlap)
                    new_n.append([n_start, nonoverlap])
                    n_start += nonoverlap
                    n_length -= nonoverlap
                    overlap = min(rule_length, n_length)
                    new_n.append([dst, overlap])

                    n_start += overlap
                    n_length -= overlap
                    #print(" - Overlap", dst, overlap)
                    #print(" - New n", n_start, n_length)
                    #if dst == 0:
                        #print("xddd", dst, src, rule_length, n_start, n_length, overlap)
                        #print(rule)
            if n_length > 0:
                #print("No overlap with rule", n_start, n_length)
                new_n.append([n_start, n_length])

        n = new_n
        print("Total seeds", sum([x[1] for x in n]), len(n))
    print("Done")
    for i in n:
        print(i)
    #print(n)
    return min([x[0] for x in n])


lowest = 1e100

print(seeds)

seed_parsed = []

for i in range(len(seeds)//2):
    si = i*2
    start = seeds[si]
    length = seeds[si+1]
    seed_parsed.append([start, length])

lowest = location_number_range(seed_parsed)


print(lowest)

# 55413352 is too high
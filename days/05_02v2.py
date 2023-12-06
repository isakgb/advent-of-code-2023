from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from typing import List


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
    sorted_rule = sorted(rule, key=lambda x: int(x.split()[1]))
    return [[int(y) for y in x.split()] for x in sorted_rule]

rules = [sort_rule(rule) for rule in rules]


class Rule:
    def __init__(self, dst, src, length):
        self.dst = dst
        self.src = src
        self.length = length

    def __repr__(self):
        return f"Rule(dst={self.dst}, src={self.src}, len={self.length})"


class Range:
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def apply_rule(self, rule: Rule) -> 'RangeList':
        result = RangeList([])

        if self.start + self.length <= rule.src:
            result.ranges.append(Range(self.start, self.length))
            return result
        if self.start >= rule.src + rule.length:
            result.ranges.append(Range(self.start, self.length))
            return result
        if self.start < rule.src:
            preoverlap = rule.src - self.start
            result.ranges.append(Range(self.start, preoverlap))
            overlap = min(self.length - preoverlap, rule.length)
            result.ranges.append(Range(rule.dst, self.start + preoverlap + overlap - rule.src))
            self.length -= preoverlap + overlap
            self.start += preoverlap + overlap
            if self.length > 0:
                print("self.length > 0", self.start, self.length, rule.src + rule.length)

            return result
        result.ranges.append(Range(self.start, self.length))
        return result

    def __repr__(self):
        return f"Range(start={self.start}, len={self.length})"


class RangeList:
    def __init__(self, ranges):
        self.ranges = ranges

    def add_ruleset(self, rules: List[Rule]):
        pass

    def __repr__(self):
        return f"RangeList({self.ranges})"

    def __len__(self):
        return sum(r.length for r in self.ranges)


print(rules)
rules = [[Rule(dst, src, length) for dst, src, length in mappings] for mappings in rules]
print(rules)

seed_parsed = []

for i in range(len(seeds)//2):
    si = i*2
    start = seeds[si]
    length = seeds[si+1]
    seed_parsed.append(Range(start, length))

print(seed_parsed)
print(seed_parsed[0].apply_rule(rules[0][0]))
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



lowest = location_number_range(seed_parsed)


print(lowest)

# 55413352 is too high
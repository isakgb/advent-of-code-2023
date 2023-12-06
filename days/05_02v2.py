from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from typing import List


groups = get_input(5).strip()
groups = apply(groups, lambda x: x.split("\n\n"))

seeds, rules = groups[0], groups[1:]

rules = apply(rules, lambda x: x.split(":")[1].split("\n")[1:])

seeds = seeds.split(": ")[1].split()
seeds = apply(seeds, int)


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
            # Range is before rule. Don't do anything
            return result
        if self.start >= rule.src + rule.length:
            # Range is after rule. Don't do anything
            return result
        if self.start < rule.src:
            # Range starts before rule
            preoverlap = rule.src - self.start
            result.ranges.append(Range(self.start, preoverlap))
            self.length -= preoverlap
            self.start += preoverlap
        if self.start >= rule.src:
            # (Remaining) Range starts at or after the rule
            endpoint = min(rule.src + rule.length, self.start + self.length)
            overlap = endpoint - self.start

            result.ranges.append(Range(rule.dst + self.start - rule.src, overlap))
            self.length -= overlap
            self.start += overlap

        return result

    def __repr__(self):
        return f"Range(start={self.start}, len={self.length})"


class RangeList:
    def __init__(self, ranges):
        self.ranges = ranges

    def add_ruleset(self, rules: List[Rule]):
        result = RangeList([])
        for range in self.ranges:
            for rule in rules:
                result.ranges.extend(range.apply_rule(rule).ranges)
                if range.length == 0:
                    break
            if range.length > 0:
                result.ranges.append(range)
        return result

    def __repr__(self):
        return f"RangeList({self.ranges})"

    def __len__(self):
        return sum(r.length for r in self.ranges)


rules = [[Rule(dst, src, length) for dst, src, length in mappings] for mappings in rules]

seed_parsed = []

for i in range(len(seeds)//2):
    si = i*2
    start = seeds[si]
    length = seeds[si+1]
    seed_parsed.append(Range(start, length))


rangelist = RangeList(seed_parsed)

for ruleset in rules:
    rangelist = rangelist.add_ruleset(ruleset)

print(min(r.start for r in rangelist.ranges))

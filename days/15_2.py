from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict
from dataclasses import dataclass

from itertools import combinations, permutations, pairwise
import math


groups = get_input(15).strip()
groups = groups.split(",")

def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

s=0
boxes = {}

for g in groups:
    if g[-1] == "-":
        label = g[:-1]
        box = hash(label)
        if box not in boxes:
            continue
        boxes[box] = [b for b in boxes[box] if b[0] != label]
    else:
        label, focal = g.split("=")
        box = hash(label)
        if box not in boxes:
            boxes[box] = []
        idx = -1
        for i, b in enumerate(boxes[box]):
            if b[0] == label:
                idx = i
                break
        if idx == -1:
            boxes[box].append([label, int(focal)])
        else:
            boxes[box][idx][1] = int(focal)

s=0

for box_n, box in boxes.items():
    for i, b in enumerate(box):
        s += (box_n+1)*(i+1)*b[1]


print(s)

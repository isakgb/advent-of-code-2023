from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict

groups = get_input(10).strip()


groups = groups.split()


width = len(groups[0])
height = len(groups)


def find_start():
    for x in range(width):
        for y in range(height):
            if groups[y][x] == 'S':
                return x, y


def dir4_mod(tile):
    if tile == '-':
        return [(1,0), (-1,0)]
    if tile == '|':
        return [(0,1), (0,-1)]
    if tile == '7':
        return [(-1,0), (0,1)]
    if tile == 'J':
        return [(-1,0), (0,-1)]
    if tile == 'L':
        return [(1,0), (0,-1)]
    if tile == 'F':
        return [(1,0), (0,1)]
    if tile == 'S':
        return [(0,1), (0,-1), (1,0), (-1,0)]


x, y = find_start()

visited = set()
distances = {}
distances[(x,y)] = 0

to_visit = [(x,y)]
visited.add((x,y))


max_dist = 0

while len(to_visit) > 0:
    x, y = to_visit.pop(0)
    for dx, dy in dir4_mod(groups[y][x]):
        if y + dy < 0 or y + dy >= height or x + dx < 0 or x + dx >= width:
            continue
        if dx == 1 and groups[y+dy][x+dx] not in '-7J':
            continue
        if dx == -1 and groups[y+dy][x+dx] not in '-LF':
            continue
        if dy == -1 and groups[y+dy][x+dx] not in '|7F':
            continue
        if dy == 1 and groups[y+dy][x+dx] not in '|JL':
            continue
        if (x+dx, y+dy) in visited:
            continue

        visited.add((x+dx, y+dy))
        to_visit.append((x+dx, y+dy))
        distances[(x+dx, y+dy)] = distances[(x,y)] + 1
        max_dist = max(max_dist, distances[(x+dx, y+dy)])
print(max_dist)

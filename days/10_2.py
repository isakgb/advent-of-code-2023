from aoc import get_input, split_double_newline, ints, floats, apply, dir8, dir4
from collections import defaultdict

groups = get_input(10).strip()


groups = groups.split()

groups = [list(row) for row in groups]


width = len(groups[0])
height = len(groups)


transformed_input = [["."]*width*3 for _ in range(height*3)]


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


# prune
for x in range(width):
    for y in range(height):
        if groups[y][x] != '.' and (x,y) not in visited:
            groups[y][x] = '.'


for y in range(height):
    for x in range(width):
        big_tile = None
        if groups[y][x] == 'S':
            big_tile = [".|.", "-S-", ".|."]
        elif groups[y][x] == 'F':
            big_tile = ["...", ".F-", ".|."]
        elif groups[y][x] == '7':
            big_tile = ["...", "-7.", ".|."]
        elif groups[y][x] == 'J':
            big_tile = [".|.", "-J.", "..."]
        elif groups[y][x] == 'L':
            big_tile = [".|.", ".L-", "..."]
        elif groups[y][x] == '-':
            big_tile = ["...", "---", "..."]
        elif groups[y][x] == '|':
            big_tile = [".|.", ".|.", ".|."]
        if big_tile:
            for dy in range(3):
                for dx in range(3):
                    transformed_input[y*3+dy][x*3+dx] = big_tile[dy][dx]


def flood(inp, x, y):
    to_visit = [(x,y)]
    visited = set()

    if inp[y][x] != '.':
        return ((x,y), 0)


    tiles = []

    visited.add((x,y))
    tiles.append((x,y))

    while len(to_visit) > 0:
        next = to_visit.pop(0)
        x, y = next
        for nx, ny in dir4(x,y):
            if nx < 0 or nx >= len(inp[0]) or ny < 0 or ny >= len(inp):
                return ((x,y), 0)
            if (nx, ny) in visited:
                continue
            if inp[ny][nx] == '.':
                to_visit.append((nx, ny))
                tiles.append((nx, ny))
                visited.add((nx, ny))

    lowest_tile = min(tiles, key=lambda t: t[1]*100000 + t[0])
    return lowest_tile, len(tiles)


floods = set()

for y in range(height):
    for x in range(width):
        f = flood(groups, x, y)
        if f[1] > 0:
            floods.add(f)


floods = [f for f in floods if flood(transformed_input, f[0][0]*3+1, f[0][1]*3+1)[1] > 0]

print(sum([f[1] for f in floods]))

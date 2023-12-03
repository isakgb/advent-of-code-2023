from aoc import get_input, split_double_newline, ints, floats, apply


groups = get_input(3).strip()

groups = apply(groups, lambda x: x.split("\n"))

groups = groups


width = len(groups[0])
height = len(groups)


print(groups)


def dirs(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1
    yield x+1, y+1
    yield x-1, y-1
    yield x+1, y-1
    yield x-1, y+1


sum_of_parts = 0

part_number_locations = set()

for x in range(width):
    for y in range(height):
        numbers = []
        symbol = groups[y][x]
        if symbol != "." and symbol not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print(symbol)
            for dx, dy in dirs(x, y):
                if 0 <= dx < width and 0 <= dy < height:
                    if groups[dy][dx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        start_x = dx
                        end_x = dx
                        while groups[dy][start_x] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            start_x -= 1
                            if start_x < 0:
                                break
                        while groups[dy][end_x] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            end_x += 1
                            if end_x >= width:
                                break
                        end_x -= 1
                        start_x += 1
                        loc = (dy, start_x)
                        if loc in part_number_locations:
                            print("already found", loc)
                            continue
                        part_number_locations.add(loc)
                        part_number = groups[dy][start_x:end_x+1]
                        print(symbol, part_number)
                        #sum_of_parts += int(part_number)
                        numbers.append(int(part_number))
        if len(numbers) == 2 and symbol == "*":
            print("found", numbers, numbers[0] * numbers[1])
            sum_of_parts += numbers[0] * numbers[1]


print(sum_of_parts)

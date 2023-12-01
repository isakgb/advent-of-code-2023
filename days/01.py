from aoc import get_input, split_double_newline, ints, floats, apply


groups = get_input(1)


groups = groups.split()

print(groups)
s=0


nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for g in groups:

    print(g)

    first_str = None
    last_str = None
    first_i = 10000
    last_i = -1000
    for n in nums:
        if n in g:
            i = g.index(n)
            i2 = g.rindex(n)
            if first_str is None:
                first_str = n
                first_i = i
            else:
                if i < first_i:
                    first_str = n
                    first_i = i
            if last_str is None:
                last_str = n
                last_i = i2
            else:
                if i2 > last_i:
                    last_str = n
                    last_i = i2

    reversed_nums = nums[::-1]
    if first_str is not None:
        first = str(int(nums.index(first_str)+1))
        if g == "bxbzngmpds28":
            print("first", first)
    if last_str is not None:
        last = str(int((9-reversed_nums.index(last_str))))

    print(first_i, last_i)

    for i, l in enumerate(g):
        if l in valid_digits:
            if first_str is None or (i < first_i):
                first = l
                first_i = i
                first_str="smh"
            if last_str is None or (i > last_i):
                last = l
                last_i = i
                last_str="smh"

    print("firstlast", first, last)
    a = int(first+last)
    print(a)
    s+=a

print(s)


# incorrect: 54451, 54449
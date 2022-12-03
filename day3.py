"""day3
"""

file1 = open('./data/day3.txt', 'r')
lines = [line.strip() for line in file1.readlines()]

lower_ord = ord("a") - 1
upper_ord = ord("A") - 1


def get_part1(lines):
    val = 0
    for line in lines:
        half_len = len(line) // 2
        first_cmp = line[:half_len]
        second_cmp = line[half_len:]

        intersections = set(first_cmp).intersection(set(second_cmp))
        for inter in intersections:
            if inter.islower():
                val += (ord(inter) - lower_ord)
            else:
                val += (ord(inter) - upper_ord) + 26
    return val


def get_part2(lines):
    val = 0
    for line1, line2, line3 in zip(lines[::3], lines[1::3], lines[2::3]):

        intersections = set(line1).intersection(set(line2)).intersection(set(line3))
        print(intersections)
        for inter in intersections:
            if inter.islower():
                val += (ord(inter) - lower_ord)
            else:
                val += (ord(inter) - upper_ord) + 26
    return val

print(get_part1(lines))
print(get_part2(lines))

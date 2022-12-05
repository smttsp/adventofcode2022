from utils import read_file

lines = read_file("./data/day4.txt")


def get_part1():
    cnt = 0
    for line in lines:
        a, b = line.split(",")
        beg_a, end_a = [int(x) for x in a.split("-")]
        beg_b, end_b = [int(x) for x in b.split("-")]
        if (
            (beg_a <= beg_b and end_a >= end_b)
            or (beg_b <= beg_a and end_b >= end_a)
        ):
            cnt += 1
    return cnt


def get_part2():
    cnt = len(lines)
    for line in lines:
        a, b = line.split(",")
        beg_a, end_a = [int(x) for x in a.split("-")]
        beg_b, end_b = [int(x) for x in b.split("-")]
        if beg_a > end_b or beg_b > end_a:
            cnt -= 1
    return cnt

print(get_part1())
print(get_part2())

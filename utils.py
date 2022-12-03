"""common utility functions

"""


def read_file(filename):
    file1 = open(filename, "r")
    lines = [line.strip() for line in file1.readlines()]
    return lines

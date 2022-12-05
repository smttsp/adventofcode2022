from collections import deque
from utils import read_file

lines = read_file("./data/day5.txt")
lists = [list() for _ in range(9)]

for line in lines:
    if "[" not in line:
        break
    vals = [x.replace("[", "").replace("]", "") for x in line.split(" ") if x.strip()]
    for idx, val in enumerate(vals):
        if val != ".":
            lists[idx].append(val)

stacks = []
for a_list in lists:
    stack = deque()
    for val in a_list[::-1]:
        stack.append(val)
    stacks.append(stack)


def get_part1():
    for line in lines:
        if "move" not in line:
            continue
        parts = [int(x) for x in line.replace("move", "").replace("from", "").replace("to","").split(" ") if x.strip()]
        count = parts[0]
        _from = parts[1] - 1
        _to = parts[2] - 1

        for _ in range(count):
            stacks[_to].append(stacks[_from].pop())

    result = ""
    for stack in stacks:
        result += stack.pop()
    return result


def get_part2():
    for line in lines:
        if "move" not in line:
            continue
        parts = [int(x) for x in line.replace("move", "").replace("from", "").replace("to","").split(" ") if x.strip()]
        count = parts[0]
        _from = parts[1] - 1
        _to = parts[2] - 1

        a_list = [stacks[_from].pop() for _ in range(count)][::-1]
        [stacks[_to].append(x) for x in a_list]

    result = ""
    for stack in stacks:
        result += stack.pop()
    return result

print(get_part2())

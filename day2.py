"""Day 2: Rock Paper Scissors
"""
file1 = open('./data/day2.txt', 'r')
lines = [line.strip() for line in file1.readlines()]

lose, draw, win = 0, 3, 6
winning_point_dict = {("A", "Y"): win, ("B", "Z"): win, ("C", "X"): win, ("A", "X"): draw, ("B", "Y"): draw, ("C", "Z"): draw}
selection_point_dict = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
winning_point_dict_part2 = {"X": lose, "Y": draw, "Z": win}

def get_part1():

    total_point = 0
    for line in lines:
        opponent, response = line.strip().split(" ")
        selection_point = selection_point_dict[response]
        won_point = draw if opponent == response else winning_point_dict.get((opponent, response), lose)
        cur_game = selection_point + won_point
        total_point += cur_game
    return total_point


def get_part2():
    file1 = open('./data/day2.txt', 'r')
    lines = file1.readlines()

    total_point = 0
    for line in lines:
        opponent, response = line.strip().split(" ")
        selection_point = selection_point_dict[response]
        if response == "X":
            cur_pt = {"A": 3, "B": 1, "C": 2}[opponent]
        elif response == "Y":
            cur_pt = {"A": 1, "B": 2, "C": 3}[opponent]
        else:
            cur_pt = {"A": 2, "B": 3, "C": 1}[opponent]
        won_point = winning_point_dict_part2[response]
        cur_game = won_point + cur_pt
        total_point += cur_game
    return total_point


# part1 = get_part1()
# print(part1)

print(get_part2())
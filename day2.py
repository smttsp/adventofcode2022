"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""

lose, draw, win = 0, 3, 6
winning_point_dict = {("A", "Y"): win, ("B", "Z"): win, ("C", "X"): win, ("A", "X"): draw, ("B", "Y"): draw, ("C", "Z"): draw}
selection_point_dict = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
winning_point_dict_part2 = {"X": lose, "Y": draw, "Z": win}

def get_part1():
    file1 = open('./data/day2.txt', 'r')
    lines = file1.readlines()

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
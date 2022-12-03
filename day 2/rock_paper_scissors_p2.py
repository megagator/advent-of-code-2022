from pprint import pprint


ROCK     = 1
PAPER    = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN  = 6

#                   opponent
#              rock | paper | sciss
#        rock |  D  |   L   |   W
#  you  paper |  W  |   D   |   L
#       sciss |  L  |   W   |   D

def get_move(goal, opp_move):
    if goal == WIN:
        return opp_move % 3 + 1
    if goal == LOSE:
        return (opp_move + 1) % 3 + 1

    # draw
    return opp_move

def generate_outcomes():
    opponent_moves = ['A',  'B',   'C']
    points         = [ ROCK, PAPER, SCISSORS]
    goals          = ['X',  'Y',   'Z']
    goal_scores    = [ LOSE, DRAW,  WIN]

    possible_outcomes = {}
    for opp_move, opp_score in zip(opponent_moves, points):
        for goal, score in zip(goals, goal_scores):
            move = get_move(score, opp_score)

            play = f'{opp_move} {goal}'
            possible_outcomes[play] = score + move

    return possible_outcomes

with open('input.txt') as f:
    content = f.read().splitlines()

all_outcomes = generate_outcomes()
total_score = 0
for line in content:
    total_score += all_outcomes[line]

print(total_score)


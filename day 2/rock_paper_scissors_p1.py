from pprint import pprint


ROCK     = 1
PAPER    = 2
SCISSORS = 3

#                   opponent
#              rock | paper | sciss
#        rock |  D  |   L   |   W
#  you  paper |  W  |   D   |   L
#       sciss |  L  |   W   |   D

def generate_outcomes():
    opponent_moves = ['A',  'B',   'C']
    your_moves     = ['X',  'Y',   'Z']
    points         = [ ROCK, PAPER, SCISSORS]

    possible_outcomes = {}
    for opp_move, opp_score in zip(opponent_moves, points):
        for move, score in zip(your_moves, points):
            match_score = (score - opp_score - 2) % 3 * 3

            play = f'{opp_move} {move}'
            possible_outcomes[play] = match_score + score

    return possible_outcomes

with open('input.txt') as f:
    content = f.read().splitlines()

all_outcomes = generate_outcomes()
# pprint(all_outcomes)
total_score = 0
for line in content:
    total_score += all_outcomes[line]

print(total_score)


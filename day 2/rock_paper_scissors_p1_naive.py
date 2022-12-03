ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6


def generate_outcomes():
    opponent_moves = ['A', 'B', 'C']
    your_moves = ['X', 'Y', 'Z']
    points = [ROCK, PAPER, SCISSORS]

    possible_outcomes = {}
    for opp_move, opp_score in zip(opponent_moves, points):
        for move, score in zip(your_moves, points):
            if any([
                    opp_score == ROCK and score == PAPER,
                    opp_score == PAPER and score == SCISSORS,
                    opp_score == SCISSORS and score == ROCK,
            ]):
                match_score = WIN
            elif any([
                    opp_score == PAPER and score == ROCK,
                    opp_score == SCISSORS and score == PAPER,
                    opp_score == ROCK and score == SCISSORS,
            ]):
                match_score = LOSE
            else:
                match_score = DRAW

            play = f'{opp_move} {move}'
            possible_outcomes[play] = match_score + score

    return possible_outcomes


with open('input.txt') as f:
    content = f.read().splitlines()

all_outcomes = generate_outcomes()
total_score = 0
for line in content:
    total_score += all_outcomes[line]

print(total_score)
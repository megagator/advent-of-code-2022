from pprint import pprint
import re


with open('input.txt') as f:
    content = f.read().splitlines()

crates = []
moves = []

instruction_stage = 'crates'
crate_regex = r"(\[[A-Z]\]\s?|\s{4})?"
move_regex = r"move (\d+) from (\d+) to (\d+)"

for line in content:
    if line == '':
        instruction_stage = 'moves'

    if instruction_stage == 'crates':
        # the crate map:
        matches = re.finditer(crate_regex, line)
        if matches:
            for match_num, match in enumerate(matches, start=1):
                m = match.group(0).strip()
                if m != '':
                    while len(crates) <= match_num:
                        crates.append([])
                    
                    crate = re.sub(r'[\[\]\s]', '', m)
                    crates[match_num].insert(0, crate)
    else:
        # the move instructions:
        match = re.match(move_regex, line)
        if match is not None:
            amount, source, destination = [int(m) for m in match.groups()]
            moves.append([amount, source, destination])

for move in moves:
    amount, source, destination = move
    lifted = [crates[source].pop() for _ in range(amount)]
    lifted.reverse()
    crates[destination].extend(lifted)


top_crates = ''.join([c.pop() for c in crates if len(c) > 0])
print(top_crates)
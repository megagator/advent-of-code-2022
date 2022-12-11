import re


CYCLE = 0
X = 1

with open('input.txt') as f:
    instructions = f.read().splitlines()

instruct_type_cycle_count = {
    'addx': 2,
    'noop': 1
}

key_cycles = []
for inx in instructions:
    command = re.sub(r'\s-?\d*', '', inx)
    for i in range(instruct_type_cycle_count[command]):
        CYCLE += 1

        if (CYCLE - 20) % 40 == 0:
            key_cycles.append(X * CYCLE)
            print(CYCLE, end=': ')
            print(X * CYCLE)

        if command == 'addx':
            if i == 1:
                _, arg = inx.split(' ')
                X += int(arg)

print(sum(key_cycles))
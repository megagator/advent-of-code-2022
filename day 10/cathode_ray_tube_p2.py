import re


CYCLE = 0
X = 1

with open('input.txt') as f:
    instructions = f.read().splitlines()

instruct_type_cycle_count = {
    'addx': 2,
    'noop': 1
}

for inx in instructions:
    command = re.sub(r'\s-?\d*', '', inx)
    for i in range(instruct_type_cycle_count[command]):
        CYCLE += 1

        if CYCLE % 40 == 1:
            print()
            print(f"Cycle {format(CYCLE, '3d')} ", end='')

        crt_pos = (CYCLE - 1) % 40
        if crt_pos in [X-1, X, X+1]:
            print('#', end='')
        else:
            print('.', end='')

        if command == 'addx':
            if i == 1:
                _, arg = inx.split(' ')
                X += int(arg)

print()
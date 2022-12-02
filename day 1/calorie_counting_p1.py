with open('input.txt') as f:
    content = f.read().splitlines()

elves = []
current_elf = 0
for line in content:
    if line == '':
        elves.append(current_elf)
        current_elf = 0
        continue

    current_elf += int(line)

loaded_elf = max(elves)
print(loaded_elf)
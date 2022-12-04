import re


with open('input.txt') as f:
    content = f.read().splitlines()

overlaps = 0
regex = r"(\d+)-(\d+),(\d+)-(\d+)"
for line in content:
    m = re.match(regex, line)
    elf1 = [int(d) for d in m.group(1,2)]
    elf2 = [int(d) for d in m.group(3,4)]

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        # elf 1 contains elf 2
        overlaps += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        # elf 2 contains elf 1
        overlaps += 1

print(overlaps)
import re


with open('input.txt') as f:
    content = f.read().splitlines()

overlaps = 0
regex = r"(\d+)-(\d+),(\d+)-(\d+)"
for line in content:
    m = re.match(regex, line)
    (a,b) = [int(d) for d in m.group(1,2)]
    (c,d) = [int(d) for d in m.group(3,4)]

    # a-b, c-d
    if b >= c and d >= a:
        overlaps += 1
    elif d >= a and b >= c:
        overlaps += 1

print(overlaps)
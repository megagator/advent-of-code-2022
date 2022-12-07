from pprint import pprint

SIZE = 14

with open('input.txt') as f:
    content = f.read().splitlines()

stream = content[0]

position = 0
four_previous_chars = [None] * SIZE
for char in stream:
    position += 1

    if four_previous_chars[0] is None:
        four_previous_chars.pop(0)
        four_previous_chars.append(char)
        continue

    four_previous_chars.pop(0)
    four_previous_chars.append(char)
    if len(set(four_previous_chars)) == SIZE:
        break

print(''.join(four_previous_chars))
print(f'Marker position started at {position}')
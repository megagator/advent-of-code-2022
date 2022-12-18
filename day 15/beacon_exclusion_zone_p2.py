import re

LOWER_BOUND = 0
UPPER_BOUND = 4_000_000
BOUNDS = range(LOWER_BOUND, UPPER_BOUND + 1)

regex = r"x=(-?\d+), y=(-?\d+)"
sensors = []
beacons = []
max_x = max_y = 0
with open('input.txt') as f:
    while (line := f.readline().strip()) != '':
        sensor_match, beacon_match = re.findall(regex, line)
        sensor = [int(d) for d in sensor_match]
        sensors.append(tuple(sensor))
        
        beacon = [int(d) for d in beacon_match]
        beacons.append(tuple(beacon))
        max_x = max(sensor[0], beacon[0], max_x)
        max_y = max(sensor[1], beacon[1], max_y)

def manhattan_distance(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return dx + dy


no_beacon_ranges = {}
for s, b in zip(sensors, beacons):
    manhat_dist = manhattan_distance(s,b)
    for dy in range(-manhat_dist, manhat_dist, + 1):
        y = s[1] - dy
        if y not in BOUNDS:
            continue

        half_row_length = manhat_dist - abs(dy)
        no_beacon_range = range(
            max(LOWER_BOUND, s[0] - half_row_length),
            min(s[0] + half_row_length, UPPER_BOUND) + 1
        )
        
        if y not in no_beacon_ranges:
            no_beacon_ranges[y] = []
        no_beacon_ranges[y].append(no_beacon_range)

# # print map
# for y in range(0, 21):
#     print(format(y, '2d'), end=' ')
#     for x in range(0, 21):
#         # if (x,y) in sensors:
#         #     print('S', end='')
#         # elif (x,y) in beacons:
#         #     print('B', end='')
#         if y in no_beacon_ranges:
#             match = False
#             for r in no_beacon_ranges[y]:
#                 if x in r:
#                     print('#', end='')
#                     match = True
#                     break
#             if not match:
#                 print('.', end='')
#         else:
#             print('.', end='')
#     print()

beacon_loc = (0,0)
for y, ranges in no_beacon_ranges.items():
    ranges.sort(key=lambda r: r[0])
    merged = [ranges[0]]
    for current in ranges:
        previous = merged[-1]
        if current[0] <= previous[-1] + 1:
            merged[-1] = range(previous[0], max(previous[-1], current[-1]) + 1)
        else:
            merged.append(current)

    if len(merged) > 1:
        x = merged[0][-1] + 1
        beacon_loc = (x,y)

print(beacon_loc)
print(beacon_loc[0] * 4_000_000 + beacon_loc[1])
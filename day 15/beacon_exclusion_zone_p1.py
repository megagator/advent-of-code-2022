import re

SEARCH_ROW = 2_000_000
# SEARCH_ROW = 10
regex = r"x=(-?\d+), y=(-?\d+)"
sensors = []
beacons = []
max_x = max_y = 0
with open('day 15/input.txt') as f:
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


no_beacon_ranges = []
for s, b in zip(sensors, beacons):
    manhat_dist = manhattan_distance(s,b)
    if SEARCH_ROW not in range(s[1]-manhat_dist, s[1]+manhat_dist+1):
        continue
    
    search_row_dist = abs(s[1] - SEARCH_ROW)
    half_row_length = manhat_dist - search_row_dist 
    no_beacon_range = range(s[0] - half_row_length, s[0] + half_row_length + 1)
    no_beacon_ranges.append(no_beacon_range)

# # print map
# for y in range(9, 12):
#     print(format(y, '2d'), end=' ')
#     for x in range(-10, 35):
#         if (x,y) in sensors:
#             print('S', end='')
#         elif (x,y) in beacons:
#             print('B', end='')
#         elif y == SEARCH_ROW:
#             match = False
#             for r in no_beacon_ranges:
#                 if x in r:
#                     print('#', end='')
#                     match = True
#                     break
#             if not match:
#                 print('.', end='')

#         else:
#             print('.', end='')
#     print()


discrete_ranges = []
for r in no_beacon_ranges:
    if len(discrete_ranges) == 0:
        discrete_ranges.append(r)
        continue

    for i, dr in enumerate(discrete_ranges):
        # overlap?
        if dr[-1] > r[0] or r[-1] > dr[0]:
            discrete_ranges.pop(i)
            discrete_ranges.append(range(min(r[0], dr[0]), max(r[-1], dr[-1])+1))
        else:
            # no overlap
            discrete_ranges.append(r)

total = 0
for dr in discrete_ranges:
    total += len(dr)

for b in set(beacons):
    if b[1] == SEARCH_ROW:
        total -= 1
for s in sensors:
    if s[1] == SEARCH_ROW:
        total -= 1

print(total)
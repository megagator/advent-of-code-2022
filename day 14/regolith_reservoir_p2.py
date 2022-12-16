with open('input.txt') as f:
    walls = f.read().splitlines()

x_min = 1_000_000
x_max = 0
y_max = 0

rock_points = set()
for wall in walls:
    joints = wall.split(' -> ')
    for i in range(1, len(joints)):
        start = [int(j) for j in joints[i-1].split(',')]
        end = [int(j) for j in joints[i].split(',')]
        if end[0] == start[0]:
            # x is same, vertical column of rock
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                rock_points.add((start[0], y))
                y_max = max(y_max, y)
        else:
            # y is same, horizontal row of rock
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                rock_points.add((x, start[1]))
                x_min = min(x_min, x)
                x_max = max(x_max, x)

x_inifite_floor = y_max + 2

# generate sand
sand_points = set()
active_sand = (500,0)
while True:
    # check if active sand can fall
    below = (active_sand[0], active_sand[1]+1)
    if below in rock_points or below in sand_points or below[1] == x_inifite_floor:
        # below is blocked, check left diag
        left_down = (active_sand[0]-1, active_sand[1]+1)
        if left_down in rock_points or left_down in sand_points or left_down[1] == x_inifite_floor:
            # left diag is blocked, check right diag
            right_down = (active_sand[0]+1, active_sand[1]+1)
            if right_down in rock_points or right_down in sand_points or right_down[1] == x_inifite_floor:
                # done falling, start again
                sand_points.add(active_sand)
                if active_sand == (500,0):
                    # we've filled the cave
                    break
                active_sand = (500,0)
            else:
                active_sand = right_down
        else:
            active_sand = left_down
    else:
        active_sand = below

    # check if we're at the floor
    if active_sand[1] == x_inifite_floor:
        sand_points.add(active_sand)
        active_sand = (500,0)

# print cave
for y in range(0, y_max+3):
    print(format(y, '3d'), end=' ')
    for x in range(x_min - 10, x_max+11):
        if (x,y) in rock_points or y == y_max + 2:
            print('#', end='')
        elif (x,y) in sand_points:
            print('O', end='')
        elif (x,y) == (500,0):
            print('+', end='')
        else:
            print('.', end='')

    print()

print()
print(len(sand_points))
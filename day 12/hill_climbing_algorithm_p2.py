with open('day 12/input.txt') as f:
    map_rows = f.read().splitlines()

# (y,x) column major 2D array
end   = (0,0)
for col, row in enumerate(map_rows):
    s = row.find('S')
    e = row.find('E')
    if s > -1:
        map_rows[col] = row.replace('S', 'a')
    if e > -1:
        map_rows[col] = map_rows[col].replace('E', 'z')
        end = (col, e)

visited_map = [[False for _ in range(len(map_rows[0]))] for _ in range(len(map_rows))]
visited_map[end[0]][end[1]] = True
shortest_map = [[10_000 for _ in range(len(map_rows[0]))] for _ in range(len(map_rows))]
shortest_map[end[0]][end[1]] = 0


points_to_visit = [end]
while (len(points_to_visit) > 0):
    # sort by shortest known path
    points_to_visit.sort(key=lambda pt: shortest_map[pt[0]][pt[1]])
    
    pt = points_to_visit.pop(0)

    move_count = shortest_map[pt[0]][pt[1]]
    north = south = east = west = None
    if pt[0] > 0:
        north = (pt[0] - 1, pt[1])
    if pt[0] < len(map_rows) - 1:
        south = (pt[0] + 1, pt[1])
    if pt[1] < len(map_rows[0]) - 1:
        east = (pt[0], pt[1] + 1)
    if pt[1] > 0:
        west = (pt[0], pt[1] - 1)

    for mv in [north, south, east, west]:
        if mv is None:
            continue

        if ord(map_rows[mv[0]][mv[1]]) + 1 < ord(map_rows[pt[0]][pt[1]]):
            continue

        if shortest_map[mv[0]][mv[1]] > move_count:
            shortest_map[mv[0]][mv[1]] = move_count + 1
        if not visited_map[mv[0]][mv[1]]:
            visited_map[mv[0]][mv[1]] = True
            points_to_visit.append(mv)

all_a_paths = []
for y, col in enumerate(shortest_map):
    for x, row in enumerate(col):
        if map_rows[y][x] == 'a':
            all_a_paths.append(shortest_map[y][x])

print(min(all_a_paths))
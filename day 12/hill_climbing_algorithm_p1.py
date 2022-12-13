with open('day 12/input.txt') as f:
    map_rows = f.read().splitlines()

# (y,x) column major 2D array
start = (0,0)
end   = (0,0)
for col, row in enumerate(map_rows):
    s = row.find('S')
    e = row.find('E')
    if s > -1:
        map_rows[col] = row.replace('S', 'a')
        start = (col, s)
    if e > -1:
        map_rows[col] = map_rows[col].replace('E', 'z')
        end = (col, e)

visited_map = [[False for _ in range(len(map_rows[0]))] for _ in range(len(map_rows))]
visited_map[start[0]][start[1]] = True
shortest_map = [[10_000 for _ in range(len(map_rows[0]))] for _ in range(len(map_rows))]
shortest_map[start[0]][start[1]] = 0


points_to_visit = [start]
while (len(points_to_visit) > 0):
    # sort by elevation, preferring higher
    points_to_visit.sort(key=lambda pt: map_rows[pt[0]][pt[1]])
    
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

        if ord(map_rows[pt[0]][pt[1]]) + 1 < ord(map_rows[mv[0]][mv[1]]):
            continue

        if shortest_map[mv[0]][mv[1]] > move_count:
            shortest_map[mv[0]][mv[1]] = move_count + 1
        if not visited_map[mv[0]][mv[1]]:
            visited_map[mv[0]][mv[1]] = True
            points_to_visit.append(mv)

print(shortest_map[end[0]][end[1]])
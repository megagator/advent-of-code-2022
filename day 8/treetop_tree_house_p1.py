from pprint import pprint

class NestedLoopBreak(Exception):
    pass

with open('input.txt') as f:
    map = f.read().splitlines()

y_max = len(map) - 1
x_max = len(map[0]) - 1

# debug = [ ['0'] * (y_max+1) for _ in range(x_max+1) ]
visible = 0
for y, row in enumerate(map):
    for x, tree in enumerate(row):
        try:
            if x == 0 or x == x_max or y == 0 or y == y_max:
                # edges are always visible
                # debug[y][x] = '1'
                visible += 1
                continue

            # north
            for n in range(y - 1, -1, -1):
                if map[n][x] < tree:
                    if n == 0:
                        # is visible from edge
                        # debug[y][x] = '↑'
                        visible += 1
                        raise NestedLoopBreak
                else:
                    break # not visible from this edge
            
            # south
            for s in range(y + 1, y_max + 1):
                if map[s][x] < tree:
                    if s == x_max:
                        # is visible from edge
                        # debug[y][x] = '↓'
                        visible += 1
                        raise NestedLoopBreak
                else:
                    break # not visible from this edge
            
            # east
            for e in range(x + 1, x_max + 1):
                if map[y][e] < tree:
                    if e == x_max:
                        # is visible from edge
                        # debug[y][x] = '→'
                        visible += 1
                        raise NestedLoopBreak
                else:
                    break # not visible from this edge
            
            # west
            for w in range(x - 1, -1, -1):
                if map[y][w] < tree:
                    if w == 0:
                        # is visible from edge
                        # debug[y][x] = '←'
                        visible += 1
                else:
                    break # not visible
        except NestedLoopBreak:
            pass

print(visible)
# pprint(debug)

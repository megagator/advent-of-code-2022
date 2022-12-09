with open('input.txt') as f:
    map = f.read().splitlines()

y_max = len(map) - 1
x_max = len(map[0]) - 1

max_visible = 0
for y, row in enumerate(map):
    for x, tree in enumerate(row):
        if x == 0 or x == x_max or y == 0 or y == y_max:
            # edges always yield a score of 0
            continue

        # north
        n_score = 0
        for n in range(y - 1, -1, -1):
            n_score += 1
            if map[n][x] >= tree:
                break # no more visiblility in this direction
        
        # south
        s_score = 0
        for s in range(y + 1, y_max + 1):
            s_score += 1
            if map[s][x] >= tree:
                break # no more visiblility in this direction
        
        # east
        e_score = 0
        for e in range(x + 1, x_max + 1):
            e_score += 1
            if map[y][e] >= tree:
                break # no more visiblility in this direction
        
        # west
        w_score = 0
        for w in range(x - 1, -1, -1):
            w_score += 1
            if map[y][w] >= tree:
                break # no more visiblility in this direction
        
        score = n_score * s_score * e_score * w_score 
        max_visible = max(max_visible, score)


print(max_visible)
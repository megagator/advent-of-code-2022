def is_touching(pt1, pt2):
    delta_x = abs(pt1[0] - pt2[0])
    delta_y = abs(pt1[1] - pt2[1])

    if delta_x <= 1 and delta_y <= 1:
        return True

    return False


with open('input.txt') as f:
    moves = f.read().splitlines()


head = tail = (0,0)
tail_history = set()
tail_history.add(tail)

for move in moves:
    direction, magnitude = move.split(' ')

    step = (0,0)
    if direction == 'R':
        step = (1,0)
    elif direction == 'L':
        step = (-1,0)
    elif direction == 'U':
        step = (0,1)
    elif direction == 'D':
        step = (0,-1)
    else:
        raise ValueError(direction)
    
    for _ in range(int(magnitude)):
        old_head = head
        head = (head[0] + step[0], head[1] + step[1])
        if not is_touching(head, tail):
            tail = old_head
            tail_history.add(tail)


print(len(tail_history))
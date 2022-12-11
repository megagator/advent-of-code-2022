def add_points(pt1, pt2):
    return (pt1[0] + pt2[0], pt1[1] + pt2[1])

def is_touching(pt1, pt2):
    delta_x = abs(pt1[0] - pt2[0])
    delta_y = abs(pt1[1] - pt2[1])

    if delta_x <= 1 and delta_y <= 1:
        return True

    return False

def catch_up_step(head, tail):
    x = head[0] - tail[0]
    y = head[1] - tail[1]
    dx = x if x == 0 else int(x/abs(x))
    dy = y if y == 0 else int(y/abs(y))

    return (dx, dy)

with open('input.txt') as f:
    moves = f.read().splitlines()


rope = [(0,0)] * 10
tail_history = set()
tail_history.add(rope[9])


steps = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1),
}

for move in moves:
    direction, magnitude = move.split(' ')
    step = steps[direction]
    
    for _ in range(int(magnitude)):
        rope[0] = add_points(rope[0], step)

        for i in range(1, len(rope)):
            if not is_touching(rope[i-1], rope[i]):
                c_u_step = catch_up_step(rope[i-1], rope[i])
                rope[i] = add_points(rope[i], c_u_step)
                if i == len(rope) - 1:
                    tail_history.add(rope[i])
            else:
                break

        # # print the rope knots
        # for y in range(15, -16, -1):
        #     for x in range(-20, 21):
        #         match = False
        #         for i, r in enumerate(rope):
        #             if r[0] == x and r[1] == y:
        #                 print(i, end='')
        #                 match = True
        #                 break
        #         if not match:
        #             if x == 0 and y == 0:
        #                 print('x', end='')
        #             else:
        #                 print('.', end='')
        #     print()
        # print(rope[0])
        # print('--------------------------')
        
# # print the tail history
# for y in range(15, -16, -1):
#     for x in range(-20, 21):
#         match = False
#         for t in tail_history:
#             if t[0] == x and t[1] == y:
#                 print('#', end='')
#                 match = True
#                 break
#         if not match:
#             if x == 0 and y == 0:
#                 print('x', end='')
#             else:
#                 print('.', end='')
#     print()

print(len(tail_history))
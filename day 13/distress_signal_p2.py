from copy import deepcopy
from functools import cmp_to_key


packets = [[[2]],[[6]]]
with open('input.txt') as f:
    end = None
    while end != '':
        line = []
        exec(f'line = {f.readline().strip()}')
        packets.append(line)
        exec(f'line = {f.readline().strip()}')
        packets.append(line)

        end = f.readline()


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            return -1
        if l == r:
            return 'continue'
        else:
            return 1

    if isinstance(l, list) and isinstance(r, list):
        while(len(l) > 0):
            try:
                result = compare(l.pop(0), r.pop(0))
            except IndexError:
                # right side ran out of items
                return 1
            else:
                if type(result) == int:
                    return result
                else:
                    continue

        if len(l) == 0 and len(r) > 0:
            return -1 # left side ran out of items
        else:
            return 'continue'

    if isinstance(l, list) and type(r) == int:
        return compare(l, [r])
    if type(l) == int and isinstance(r, list):
        return compare([l], r)

def cmp_wrap(l,r):
    l_cpy = deepcopy(l)
    r_cpy = deepcopy(r)
    res = compare(l_cpy,r_cpy)
    if res == 'continue':
        return -1
    return res


packets.sort(key=cmp_to_key(cmp_wrap))
two = packets.index([[2]])
six = packets.index([[6]])

print((two + 1) * (six + 1))

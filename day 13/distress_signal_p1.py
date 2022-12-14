pairs = []
with open('input.txt') as f:
    end = None
    while end != '':
        left = right = ''
        exec(f'left = {f.readline().strip()}')
        exec(f'right = {f.readline().strip()}')
        new_pair = {
            'left': left,
            'right': right,
        }
        pairs.append(new_pair)

        end = f.readline()


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            print(f'{l} vs {r}', end='')
            return True
        if l == r:
            return 'continue'
        else:
            print(f'{l} vs {r}', end='')
            return False

    if isinstance(l, list) and isinstance(r, list):
        while(len(l) > 0):
            try:
                result = compare(l.pop(0), r.pop(0))
            except IndexError:
                # right side ran out of items
                print(f'{l} vs {r}', end='')
                return False
            else:
                if type(result) == bool:
                    return result
                else:
                    continue

        if len(l) == 0 and len(r) > 0:
            print(f'{l} vs {r}', end='')
            return True # left side ran out of items
        else:
            return 'continue'

    if isinstance(l, list) and type(r) == int:
        return compare(l, [r])
    if type(l) == int and isinstance(r, list):
        return compare([l], r)


correct_pairs = []
for i, pair in enumerate(pairs):
    l = pair['left']
    r = pair['right']

    print(f"Pair {i+1}: ", end='')
    result = compare(l,r)
    if result:
        correct_pairs.append(i+1)
    print(f'  {result}')

print(sum(correct_pairs))
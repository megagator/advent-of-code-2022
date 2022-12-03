LC_PRIORITY_ORD_DIFF = ord('a') - 1 # a = 1, ...
UC_PRIORITY_ORD_DIFF = ord('A') - 27 # A = 27, ...

with open('input.txt') as f:
    content = f.read().splitlines()

solutions = []
for line in content:
    compartment_size = int(len(line) / 2)
    compartment_1 = line[:compartment_size]
    compartment_2 = line[compartment_size:]

    unique_1 = sorted(set(compartment_1))
    unique_2 = sorted(set(compartment_2))

    i = 0
    j = 0
    while True:
        if unique_1[i] == unique_2[j]:
            solution = ord(unique_1[i]) - LC_PRIORITY_ORD_DIFF
            if solution < 0:
                solution = ord(unique_1[i]) - UC_PRIORITY_ORD_DIFF

            solutions.append(solution)
            break
        elif unique_1[i] > unique_2[j]:
            j += 1
        else:
            i += 1

print(sum(solutions))
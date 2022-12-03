LC_PRIORITY_ORD_DIFF = ord('a') - 1 # a = 1, ...
UC_PRIORITY_ORD_DIFF = ord('A') - 27 # A = 27, ...

with open('input.txt') as f:
    content = f.read().splitlines()

solutions = []
for i in range(0, len(content), 3):
    line_1 = content[i]
    line_2 = content[i+1]
    line_3 = content[i+2]
    
    unique_1 = sorted(set(line_1))
    unique_2 = sorted(set(line_2))
    unique_3 = sorted(set(line_3))

    i = j = k = 0
    while True:
        if unique_1[i] == unique_2[j] == unique_3[k]:
            solution = ord(unique_1[i]) - LC_PRIORITY_ORD_DIFF
            if solution < 0:
                solution = ord(unique_1[i]) - UC_PRIORITY_ORD_DIFF

            solutions.append(solution)
            break
        elif unique_1[i] < unique_2[j] or unique_1[i] < unique_3[k]:
            i += 1
        elif unique_2[j] < unique_3[k] or unique_2[j] < unique_1[i]:
            j += 1
        else :
            k += 1

print(sum(solutions))
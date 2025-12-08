import numpy as np

file = open("input.txt", "r")
total = 0
input = []
for line in file:
    input.append(list(line.replace("\n", "")))

transposed_data = np.transpose(input)

first_line = True
result = 0
for line in transposed_data:
    if first_line:
        operator = line[-1]
        first_line = False
        if operator == "*":
            result = 1
    elif ''.join(line).strip() == '':
        first_line = True
        total += result
        result = 0
        continue

    if operator == "*":
        result *= int(''.join(line[:-1]))
    else:
        result += int(''.join(line[:-1]))

total += result
print(total)
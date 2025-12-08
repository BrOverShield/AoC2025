file = open("Input.txt")
zeros = 0
result = 50
for line in file:
    clean_line = line.replace("\n","")
    direction = clean_line[:1]
    clicks = int(clean_line[1:])

    zeros += int(clicks/100)
    clicks %= 100

    starting_result = result

    if direction == "R":
        result += clicks
    else: # direction == "L"
        result -= clicks

    if starting_result < result:
        if (starting_result < 0 and result > 0) or (starting_result < 100 and result > 100):
            zeros += 1
    elif result < starting_result:
        if (result < 0 and starting_result > 0) or (result < 100 and starting_result > 100):
            zeros += 1

    if result % 100 == 0:
        zeros += 1
        result = 0

    if result < 0:
        result += 100

    if result > 99:
        result -= 100

print(zeros)
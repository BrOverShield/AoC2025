file = open("Input.txt")
zeros = 0
result = 50
for line in file:
    clean_line = line.replace("\n","")
    direction = clean_line[:1]
    clicks = int(clean_line[1:])%100 # %100 because some numbers are more than 100

    if direction == "R":
        result += clicks
    else: # direction == "L"
        result -= clicks

    if result < 0:
        result += 100

    if result > 99:
        result -= 100

    if result == 0:
        zeros +=1

print(zeros)
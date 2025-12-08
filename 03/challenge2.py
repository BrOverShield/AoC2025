file = open("input.txt", "r")
_sum = 0
for line in file:
    cleaned_line = line.replace("\n","")
    start_position = 0
    s_joltage = ""
    lenght = len(cleaned_line)
    for left in range(11,-1,-1):
        truncated_line = cleaned_line[start_position:lenght - left]
        #what is the highest number
        found = False
        for number in range(9,0,-1):
            for position, digit in enumerate(truncated_line):
                s_number = str(number)
                if digit == s_number:
                    s_joltage += s_number
                    found = True
                    start_position = start_position + position + 1
                    break
            if found:
                break
    _sum += int(s_joltage)
print(_sum)
    
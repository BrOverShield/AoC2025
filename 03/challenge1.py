file = open("input.txt", "r")
_sum = 0
for line in file:
    cleaned_line = line.replace("\n","")
    truncated_line = cleaned_line[:-1]
    #what is the highest number
    s_highest_number = "0"
    for number in list(range(9,0,-1)):
        s_number = str(number)
        if s_number in truncated_line:
            s_highest_number = s_number
            break
    
    #get all the positions of the highest number
    first_position = 0
    for position, s_number in enumerate(truncated_line):
        if s_number == s_highest_number:
            first_position = position
            break
    
    truncated_line = cleaned_line[first_position + 1:]
    found = 0
    for number in range(9,0,-1):
        s_number = str(number)
        for digit in truncated_line:
            if digit == s_number:
                found = number
                break
        if found:
            break
    _sum += int(s_highest_number + str(found))
print(_sum)
    
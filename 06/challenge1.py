file = open("input.txt", "r")
total = 0
input = []
for line in file:
    clean_line = " ".join(line.split()).strip()
    if not clean_line[0] == "+" and not clean_line[0] == "*":
        input.append(clean_line.split(" "))
    else:
        for i, operator in enumerate(clean_line.split(" ")):
            if operator == "+":
                result = 0
                for numbers in input:
                    result += int(numbers[i])
            else:
                result = 1
                for numbers in input:
                    result *= int(numbers[i])
            total += result
print(total)
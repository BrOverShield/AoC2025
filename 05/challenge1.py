file = open("input.txt", "r")
ranges = []
fresh = 0
ingredients = False
for line in file:
    clean_line = line.replace("\n", "")

    if clean_line == "":
        ingredients = True
        continue

    if not ingredients:
        numbers = clean_line.split("-")
        start = int(numbers[0])
        end = int(numbers[1])
        ranges.append([start, end])
    else:
        ingredient = int(clean_line)
        for _range in ranges:
            if ingredient >= _range[0] and ingredient <= _range[1]:
                fresh += 1
                break
print(fresh)
START = 0
END = 1

file = open("input.txt", "r")
ranges = []
fresh = 1
smallest_id = None
biggest_id = None

for line in file:
    clean_line = line.replace("\n", "")

    if clean_line == "":
        break

    numbers = clean_line.split("-")
    start = int(numbers[START])
    if smallest_id == None or smallest_id > start:
        smallest_id = start
    end = int(numbers[END])
    if biggest_id == None or biggest_id < end:
        biggest_id = end
    ranges.append([start, end])

progression_id = smallest_id

while True:
    while True:
        found_range = False
        for _range in ranges:
            if _range[START] <= progression_id and _range[END] > progression_id:
                fresh += _range[END] - progression_id
                progression_id = _range[END]
                found_range = True
                break

        if not found_range:
            break

    if progression_id == biggest_id:
        break

    target = biggest_id
    for _range in ranges:
        if _range[START] > progression_id and _range[START] < target:
            target = _range[START]
    progression_id = target
    fresh += 1

print(fresh)
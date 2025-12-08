file = open("input.txt", "r")
first_line = True
positions = {}
for line in file:
    if first_line:
        first_line = False
        for i, cell in enumerate(line):
            if cell == "S":
                positions[i] = 1
    else:
        new_keys = {}
        for position in positions.keys():
            if line[position] == "^":
                if position + 1 not in new_keys:
                    new_keys[position + 1] = 0
                if position - 1 not in new_keys:
                    new_keys[position - 1] = 0

                new_keys[position + 1] += positions[position]
                new_keys[position - 1] += positions[position]

                positions[position] = 0
        for key, value in new_keys.items():
            if key not in positions:
                positions[key] = 0
            positions[key] += value

timelines = sum(positions.values())
print(timelines)

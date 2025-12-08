file = open("input.txt", "r")
first_line = True
positions = set()
splits = 0
for line in file:
    if first_line:
        first_line = False
        for i, cell in enumerate(line):
            if cell == "S":
                positions.add(i)
    else:
        positions_to_remove = []
        positions_to_add = []
        for position in positions:
            if line[position] == "^":
                positions_to_remove.append(position)
                positions_to_add.append(position - 1)
                positions_to_add.append(position + 1)
                splits += 1

        for position in positions_to_remove:
            positions.remove(position)

        for position in positions_to_add:
            (positions.add(position))

print(splits)

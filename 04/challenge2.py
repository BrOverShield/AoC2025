file = open("input.txt", "r")
_sum = 0
_map = []
for y, line in enumerate(file):
    clean_line = line.replace("\n","")
    for x, cell in enumerate(clean_line):
        if cell == "@":
            s_x = str(x)
            s_y = str(y)
            _map.append(s_x + "-" + s_y)
        
while True:
    marked_for_removal = []
    for value in _map:
        coordinates = value.split("-")
        x = int(coordinates[0])
        y = int(coordinates[1])
        too_close = 0
        for i in range(y - 1, y + 2):
            s_i = str(i)
            for j in range (x - 1, x + 2):
                if i != y or j != x:
                    s_j = str(j)
                    if s_j + "-" + s_i in _map:
                        too_close += 1
        if too_close < 4:
            marked_for_removal.append(value)

    amount_to_remove = len(marked_for_removal)
    if amount_to_remove == 0:
        break
    else:
        _sum += amount_to_remove
        for marked_roll in marked_for_removal:
            _map.remove(marked_roll)
print(_sum)
file = open("input.txt", "r")
_sum = 0
_map = []
min_x = 0
min_y = 0
max_x = 0
max_y = 0
for y, line in enumerate(file):
    max_y = y
    clean_line = line.replace("\n","")
    max_x = len(clean_line) - 1
    for x, cell in enumerate(clean_line):
        if cell == "@":
            s_x = str(x)
            s_y = str(y)
            _map.append(s_x + "-" + s_y)
        
for value in _map:
    coordinates = value.split("-")
    s_x = coordinates[0]
    s_y = coordinates[1]
    x = int(s_x)
    y = int(s_y)
    too_close = 0
    for i in range(y - 1, y + 2):
        s_i = str(i)
        for j in range (x - 1, x + 2):
            if i != y or j != x:
                s_j = str(j)
                if s_j + "-" + s_i in _map:
                    too_close += 1
    if too_close < 4:
        _sum += 1
print(_sum)
    
    
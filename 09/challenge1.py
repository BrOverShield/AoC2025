file = open ("input.txt", "r")
coordinates = []
biggest = None
for line in file:
    coordinates.append(line.replace("\n", "").split(","))

combinations = []
for a, coordinates_a in enumerate(coordinates):
    for b, coordinates_b in enumerate(coordinates):
        if a != b:
            name = ""
            if a < b:
                name = str(a) + "-" + str(b)
            else:
                name = str(b) + "-" + str(a)

            if name not in combinations:
                combinations.append(name)
                area = (abs(int(coordinates_b[0]) - int(coordinates_a[0])) + 1) * (abs(int(coordinates_b[1]) - int(coordinates_a[1])) + 1)
                if biggest == None:
                    biggest = area
                else:
                    if area > biggest:
                        biggest = area

print(biggest)

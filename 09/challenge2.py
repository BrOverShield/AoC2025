from shapely.geometry import Polygon, box

file = open ("input.txt", "r")
coordinates = []
for line in file:
    array = line.replace("\n", "").split(",")
    coordinates.append((array[0], array[1]))

poly = Polygon(coordinates)

areas = {}
for a, coordinates_a in enumerate(coordinates):
    for b, coordinates_b in enumerate(coordinates):
        if a != b:
            name = ""
            if a < b:
                name = str(a) + "-" + str(b)
            else:
                name = str(b) + "-" + str(a)

            if name not in areas:
                rectangle = (coordinates_a[0],coordinates_a[1],coordinates_b[0],coordinates_b[1])
                rect = box(*rectangle)
                if rect.within(poly):
                    areas[name] = (abs(int(coordinates_b[0]) - int(coordinates_a[0])) + 1) * (abs(int(coordinates_b[1]) - int(coordinates_a[1])) + 1)
                else:
                    areas[name] = 0

for combination in sorted(areas, key=areas.get, reverse=True):
    print(areas[combination])
    break
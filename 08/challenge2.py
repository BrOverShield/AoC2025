import math
from itertools import islice

file = open("input.txt", "r")
boxes = {}
for id, line in enumerate(file):
    coordinates = line.replace("\n","").split(",")
    x = int(coordinates[0])
    y = int(coordinates[1])
    z = int(coordinates[2])
    boxes[id] = {"x": x, "y": y, "z": z}

distances = {}

for box_a, data_a in boxes.items():
    for box_b, data_b in boxes.items():
        if box_a != box_b :
            name = ""
            if box_a < box_b:
                name = str(box_a) + "-" + str(box_b)
            else:
                name = str(box_b) + "-" + str(box_a)

            if name not in distances:
                distances[name] = math.sqrt((data_b["x"] - data_a["x"])**2 + (data_b["y"] - data_a["y"])**2 + (data_b["z"] - data_a["z"])**2)

sorted_distances = {}
for key in sorted(distances, key=distances.get):
    sorted_distances[key] = distances[key]

circuits = {}
next_circuit = 1
connections = 0
last_connection = ""
for connection_name, distance in sorted_distances.items():
    box_a = connection_name.split("-")[0]
    box_b = connection_name.split("-")[1]
    found_a = -1
    found_b = -1
    for number, circuit in circuits.items():
        if box_a in circuit:
            found_a = number

        if box_b in circuit:
            found_b = number

        if found_a != -1 and found_b != -1:
            break

    if found_a != -1 and found_b != -1:
        if found_a != found_b:
            if found_a < found_b:
                circuits[found_a] += circuits[found_b]
                circuits.pop(found_b)
            else:
                circuits[found_b] += circuits[found_a]
                circuits.pop(found_a)
        else:
            continue
    elif found_a == -1 and found_b != -1:
        circuits[found_b].append(box_a)
    elif found_b == -1 and found_a != -1:
        circuits[found_a].append(box_b)
    else: # none of them found
        circuits[next_circuit] = [box_a, box_b]
        next_circuit += 1

    last_connection = connection_name

sorted_circuits = {}
for key in sorted(circuits, key=lambda x: len(circuits[x]), reverse=True):
    sorted_circuits[key] = circuits[key]

product = 1
for number, circuit in dict(islice(sorted_circuits.items(), 3)).items():
    product *= len(circuit)

box_a = int(last_connection.split("-")[0])
box_b = int(last_connection.split("-")[1])

print(boxes[box_a]["x"] * boxes[box_b]["x"])
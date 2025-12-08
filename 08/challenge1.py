import math
from itertools import islice

file = open("input.txt", "r")
boxes = []
for id, line in enumerate(file):
    coordinates = line.replace("\n","").split(",")
    x = int(coordinates[0])
    y = int(coordinates[1])
    z = int(coordinates[2])
    boxes.append({"id": id, "x": x, "y": y, "z": z})

distances = {}

for box_a in boxes[:-1]:
    for box_b in boxes[1:]:
        if box_a["id"] != box_b["id"] :
            name = ""
            if box_a["id"] < box_b["id"]:
                name = str(box_a["id"]) + "-" + str(box_b["id"])
            else:
                name = str(box_b["id"]) + "-" + str(box_a["id"])

            if name not in distances:
                distances[name] = math.sqrt((box_b["x"] - box_a["x"])**2 + (box_b["y"] - box_a["y"])**2 + (box_b["z"] - box_a["z"])**2)

sorted_distances = {}
for key in sorted(distances, key=distances.get):
    sorted_distances[key] = distances[key]

circuits = {}
next_circuit = 1
connections = 0
target_connections = 1000
for boxes, distance in dict(islice(sorted_distances.items(), target_connections)).items():
    box_a = boxes.split("-")[0]
    box_b = boxes.split("-")[1]
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
    elif found_a == -1 and found_b != -1:
        circuits[found_b].append(box_a)
    elif found_b == -1 and found_a != -1:
        circuits[found_a].append(box_b)
    else: # none of them found
        circuits[next_circuit] = [box_a, box_b]
        next_circuit += 1

sorted_circuits = {}
for key in sorted(circuits, key=lambda x: len(circuits[x]), reverse=True):
    sorted_circuits[key] = circuits[key]

product = 1
for number, circuit in dict(islice(sorted_circuits.items(), 3)).items():
    product *= len(circuit)

print(product)
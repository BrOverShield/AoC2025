import math
from scipy.optimize import linprog
import numpy as np

def joltage_match(score, joltage_target):
    matches = True
    for i, joltage in enumerate(joltage_target):
        if i not in score:
            if joltage != 0:
                matches = False
                break
        elif joltage != score[i]:
            matches = False
            break
    return matches

file = open("input.txt", "r")
total = 0
for line in file:
    split = line.split(" ")
    joltage_target = [int(x) for x in split[-1].replace("\n","")[1:-1].split(",")]
    total_joltage = sum(joltage_target)
    buttons = split[1:-1]
    affected_lights = np.zeros((len(joltage_target), len(split[1:-1])), dtype=int)
    for button_number, button in enumerate(buttons):
        for affected_light in button[1:-1].split(","):
            affected_lights[int(affected_light)][button_number] = 1

    constraints = np.ones(len(buttons),  dtype=int)

    solution = linprog(c=constraints, A_eq=affected_lights, b_eq=joltage_target, integrality=1)
    total += int(solution.fun)

print(total)
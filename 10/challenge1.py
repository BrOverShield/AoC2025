def lights_match(score, lights):
    matches = True
    for i, light in enumerate(lights):
        if i not in score:
            if light == "#":
                matches = False
                break
        elif (light == "#" and score[i] % 2 != 1) or (light == "." and score[i] % 2 != 0):
            matches = False
    return matches

def generate_possibilities(number_of_lights,presses):
    result = []

    def backtrack(remaining, length, current):
        if length == 1:
            # Only one number left, it must be the remaining sum
            if remaining >= 0:
                result.append(current + [remaining])
            return

        for x in range(remaining + 1):
            backtrack(remaining - x, length - 1, current + [x])

    backtrack(presses, number_of_lights, [])
    return result

file = open("input.txt", "r")
total = 0
for line in file:
    split = line.split(" ")
    lights = list(split[0][1:-1])
    buttons = []
    for button in split[1:-1]:
        affected_lights = []
        for affected_light in button.replace("(","").replace(")","").split(","):
            affected_lights.append(int(affected_light))
        buttons.append(affected_lights)

    maximum_presses = 1
    while True:
        possibilities = generate_possibilities(len(buttons), maximum_presses)
        found = False
        for possibility in possibilities:
            score = {}
            for button_number, presses in enumerate(possibility):
                if presses:
                    for affected_light in buttons[button_number]:
                        if affected_light not in score:
                            score[affected_light] = 0
                        score[affected_light] += presses
            if lights_match(score, lights):
                total += maximum_presses
                found = True
                break
        if found:
            break
        maximum_presses += 1

print(total)
answer = 0
file = open ("input.txt","r")
regions = file.read().strip().split('\n\n')[-1].split('\n')
for region in regions:
    l, w = list(int(x) for x in region.split(":")[0].split("x"))
    presents =  sum(list(int(x) for x in region.split(":")[1].strip().split(" ")))
    l = int(l / 3)
    w = int(w / 3)
    if l * w >= presents:
        answer += 1

print(answer)

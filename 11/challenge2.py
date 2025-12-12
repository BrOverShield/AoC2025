from functools import lru_cache
from collections import defaultdict

connections = defaultdict(list)
file = open("input.txt","r")
for line in file:
    connection = line.replace(":","").replace("\n","").split(" ")
    connections[connection[0]] = connection[1:]

@lru_cache(None)
def find_connections(label, target_label):
    if label == target_label:
        return 1
    total = 0
    for connection in connections[label]:
        total += find_connections(connection, target_label)
    return total

svr_fft = find_connections("svr", "fft")
fft_dac = find_connections("fft", "dac")
dac_out = find_connections("dac", "out")
svr_dac = find_connections("svr", "dac")
dac_fft = find_connections("dac", "fft")
fft_out = find_connections("fft", "out")

print((svr_fft * fft_dac * dac_out) + (svr_dac * dac_fft * fft_out))


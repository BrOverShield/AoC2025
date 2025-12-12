connections = {}
file = open("input.txt","r")
for line in file:
    connection = line.replace(":","").replace("\n","").split(" ")
    connections[connection[0]] = connection[1:]

def find_connections(label, connection_count):
    for connection in connections[label]:
        if connection == "out":
            return connection_count + 1
        else:
            connection_count = find_connections(connection, connection_count)
    return connection_count

reactor_connection = 0
print(find_connections("you", reactor_connection))

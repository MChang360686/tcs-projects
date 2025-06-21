graph = []

for i in range(5):
    sublist = []
    for j in range(5):
        sublist.append(0)
    graph.append(sublist)

def print_graph():
    for i in range(len(graph)):
        print(graph[i])

def connect_vertices(a, b):
    if a < len(graph) and b < len(graph):
        graph[a][b] = 1
        graph[b][a] = 1

def wipe_graph():
    for i in range(0, len(graph)):
        for j in range(0, len(graph)):
            if graph[i][j] != 0:
                graph[i][j] = 0
            else:
                continue

connect_vertices(2, 3)
print_graph()


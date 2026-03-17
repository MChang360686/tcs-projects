class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, directed=False):
        self.adj_matrix[u][v] = 1
        if not directed:
            self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v, directed=False):
        self.adj_matrix[u][v] = 0
        if not directed:
            self.adj_matrix[v][u] = 0

    def display(self):
        print("Adjacency Matrix:")
        print("   ", " ".join(str(i) for i in range(self.num_vertices)))
        for i, row in enumerate(self.adj_matrix):
            print(f"{i}: ", " ".join(str(val) for val in row))

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = [start]
        visited[start] = True
        traversal = []

        while queue:
            vertex = queue.pop(0)
            traversal.append(vertex)

            for neighbor in range(self.num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal

    def dfs(self, start):
        visited = [False] * self.num_vertices
        traversal = []
        self._dfs_helper(start, visited, traversal)
        return traversal

    def _dfs_helper(self, vertex, visited, traversal):
        visited[vertex] = True
        traversal.append(vertex)

        for neighbor in range(self.num_vertices):
            if self.adj_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                self._dfs_helper(neighbor, visited, traversal)


# --- Demo ---
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

g.display()

print("\nBFS from vertex 0:", g.bfs(0))
print("DFS from vertex 0:", g.dfs(0))
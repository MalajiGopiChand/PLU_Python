# 20. Perform a Depth-First Search (DFS) traversal starting from vertex A.

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, vertex, visited):
        visited.append(vertex)
        print(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.DFS(i, visited)

g = Graph()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")

visited = []
g.DFS("A", visited)
# 19. Perform a Breadth-First Search (BFS) traversal starting from vertex A.
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

    def BFS(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex)

            for i in self.graph[vertex]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

g = Graph()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")

g.BFS("A")
# 18. Check whether there is a direct edge between two given vertices.

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

    def checkEdge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            print(u, v)
        else:
            print( u, v)

g = Graph()

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "D")

g.checkEdge("A", "B")
g.checkEdge("A", "D")
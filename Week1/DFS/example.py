from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
    def DFS(self, v):
        visited = [False] * (max(self.graph) + 1)

        self.DFSUtil(v, visited)

    def printEdge(self):
        print(self.graph)
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 4)
    g.addEdge(1, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(4, 4)
    g.addEdge(5, 2)
    print("DFS starts with vertex 2")
    g.printEdge()
    g.DFS(2)
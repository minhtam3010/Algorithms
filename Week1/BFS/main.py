class Graph:

    def __init__(self):
        self.graph = dict()
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def BFS(self, start):
        visited = [False for _ in range(len(self.graph))]
        idx = 0
        queue = [start]
        while idx <= len(self.graph):
            if visited[start] != True:
                print(start + 1, end=" ")
                visited[start] = True
            if len(queue) != 0:
                start = queue.pop(0)
                # print(start)
                for i in self.graph[start]:
                    if visited[i] != True and i not in queue:
                        queue.append(i)
                # print(queue)
            idx += 1

    def printGraph(self):
        print(self.graph)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(1, 3)
    g.addEdge(3, 1)
    g.addEdge(1, 4)
    g.addEdge(4, 1)
    g.addEdge(2, 4)
    g.addEdge(4, 2)
    g.addEdge(3, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 4)
    # g.printGraph()
    g.BFS(0)
    print()
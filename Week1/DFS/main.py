class Graph:

    def __init__(self):
        self.graph = dict()
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u] += [v]
        else:
            self.graph[u] = [v] 
            
    
    def searchDFS(self, start):
        idx = 0
        hold = []
        while idx < len(self.graph):
            if start not in hold:
                print(start, end=" ")
                hold.append(start)
            else:
                start = self.graph[hold[len(hold) - 2]][self.graph[start].index(start) + 1] if len(hold) != 1 else self.graph[hold[len(hold) - 1]][self.graph[start].index(start) + 1]
                continue

            start = self.graph[start][0]
            idx += 1

    def printEdge(self):
        print(self.graph)


if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(1, 0)
    graph.addEdge(2, 3)
    graph.addEdge(2, 0)
    graph.addEdge(3, 3)

    graph.printEdge()
    graph.searchDFS(1)
    print()
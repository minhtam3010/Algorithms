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
                if current not in self.graph[prev]:
                    prev = hold[hold.index(prev) - 1]
                elif len(self.graph[prev][self.graph[prev].index(current):]) != 1:
                    start = self.graph[prev][self.graph[prev].index(current):][1] # 0
                    current = start # 4
                else:
                    current = prev # 4
                    prev = hold[hold.index(prev) - 1] # 5

                continue

            prev = start
            start = self.graph[start][0]
            current = start
            idx += 1

    def printEdge(self):
        print(self.graph)


if __name__ == "__main__":
    graph = Graph()
    # graph.addEdge(0, 1)
    # graph.addEdge(0, 2)
    # graph.addEdge(0, 4)
    # graph.addEdge(1, 5)
    # graph.addEdge(1, 2)
    # graph.addEdge(2, 0)
    # graph.addEdge(2, 3)
    # graph.addEdge(3, 3)
    # graph.addEdge(4, 4)
    # graph.addEdge(5, 2)

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 4)
    graph.addEdge(0, 7)
    graph.addEdge(1, 2)
    graph.addEdge(1, 5)
    graph.addEdge(1, 6)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    graph.addEdge(4, 4)
    graph.addEdge(4, 7)
    graph.addEdge(5, 2)
    graph.addEdge(6, 5)
    graph.addEdge(7, 7)

    
    graph.printEdge()
    graph.searchDFS(2)
    print()
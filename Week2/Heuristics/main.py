import re


class Graph:

	def __init__(self, n):
		self.graph = [[0]*n for i in range(n)]
		self.hold = []
		self.res = 0
		self.idx = 0

	def addWeight(self, u, v, w):
		self.graph[u][v] = w

	def findSortPath(self, start):
		if self.idx == len(self.graph[start]):
			return
		getMin = True
		idxGraph = 0
		minPath = 0

		for i in range(len(self.graph[start])):
			if getMin and i != start and i not in self.hold:
				minPath = self.graph[start][i]
				idxGraph = i
				getMin = False
				continue
			elif i == start or getMin:
				continue
			
			if self.graph[start][i] < minPath:
				minPath = self.graph[start][i]
				idxGraph = i
		if minPath == 0:
			print("(" + str(start + 1) + " ," + str(self.hold[0] + 1) + ")" + " = " + str(self.res + self.graph[start][0]))
			# print(f"({str(start + 1)}, {str(self.hold[0][0])}) = {str(self.res + self.graph[self.hold[0]][0])}")
		else:
			print((start + 1, idxGraph + 1), end="--> ")
		self.hold.append(start)
		# print(minPath)
		self.res += minPath
		self.idx += 1
		self.findSortPath(idxGraph)
		

g = Graph(5)
g.addWeight(0, 1, 1)
g.addWeight(0, 2, 2)
g.addWeight(0, 3, 7)
g.addWeight(0, 4, 5)

g.addWeight(1, 0, 1)
g.addWeight(1, 2, 4)
g.addWeight(1, 3, 4)
g.addWeight(1, 4, 3)

g.addWeight(2, 0, 2)
g.addWeight(2, 1, 4)
g.addWeight(2, 3, 1)
g.addWeight(2, 4, 2)

g.addWeight(3, 0, 7)
g.addWeight(3, 1, 4)
g.addWeight(3, 2, 1)
g.addWeight(3, 4, 3)

g.addWeight(4, 0, 5)
g.addWeight(4, 1, 3)
g.addWeight(4, 2, 2)
g.addWeight(4, 3, 3)

g.findSortPath(0)
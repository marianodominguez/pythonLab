'''
Created on Feb 6, 2011

@author: mariano
'''

class Graph:
    def __init__(self, size):
        self.vertexList = []
        self.adjMatrix = [0] * size
        self.adjList= [ [] for i in range(size) ]

        for i in range(size):
            self.adjMatrix[i] = [0] * size
        
    def addVertex(self, v):
        self.vertexList.append(v)
    def addEdge(self, a, b):
        node1 = self.vertexList.index(a)
        node2 = self.vertexList.index(b)
        #check that nodes exist
        #avoid repetitions
        self.adjList[node1].append(node2)
        self.adjList[node2].append(node1)
        self.adjMatrix[node1][node2] = 1
        self.adjMatrix[node2][node1] = 1
    
    def dfs_path(self, a, b):
        start = self.vertexList.index(a)
        end = self.vertexList.index(b)
        stack = [start]
        path = [start]
        visited = [start]
        current = start
        while stack:
            #print stack, current
            nextNodes = self.adjList[current]
            for next in nextNodes:
                found = False
                if next not in visited:
                    stack.append(next)
                    current = next;
                    path.append(current)
                    found = True
                    break
            if not found and stack:
                current = stack.pop()
            visited.append(current)
            if current == end:
                return path
        return []

    def bfs_path(self, a, b):
        start = self.vertexList.index(a)
        end = self.vertexList.index(b)
        queue = [start]
        path = []
        visited = [start]
        current = None
        while queue:
            print queue, current
            current = queue[0]
            path.append(current)                               

            visited.append(current)
            queue.remove(current)
            if current == end:
                return path
            nextNodes = self.adjList[current]
            for n in nextNodes:                
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
        return []

    def pathValues(self, path=[]):
        return [self.vertexList[i] for i in path]

from algorithms.Graphs import Graph

g = Graph(6)
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("B", "C")
g.addEdge("C", "D")
g.addEdge("D", "E")
g.addEdge("D", "A")
g.addEdge("B", "F")

print g.adjMatrix
print g.adjList
print "BFS", g.pathValues(g.bfs_path("A","F"))
print "DFS", g.pathValues(g.dfs_path("A","F"))


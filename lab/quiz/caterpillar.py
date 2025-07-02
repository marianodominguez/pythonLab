def findCycles(graph,v1, path = []):
    pathsFound = []
    currentPath = currentPath + v1
    

def findPath(graph,v1,v2, path = []):
    path = path + [v1]
    if v1 == v2: return path
    if v1 not in graph: return []
    else:
        #remove visited links
        for v in graph[v1]:
            if v not in path:
                found = findPath(graph, v, v2 , path)
                if ( found != []):
                    return found
        return []
            
def isConnected(graph):
    for v1 in graph:
        for v2 in graph:
            if v1 != v2:
                path = findPath(graph,v1,v2)
                if path == []:
                    return False
    return True

def isAcyclic(graph):
    return True

def isCaterpillar(graph):
    return False

def addEdge(adjList, v1, v2):
    if v1 not in adjList:  
        adjList[v1] = [ v2 ]
    else:
        adjList[v1].append(v2)
    if v2 not in adjList:  
        adjList[v2] = [ v1 ]
    else:
        adjList[v2].append(v1)

def readGraph(f):
    """ 
    Reads the graphic form a text file the text file should be already open
    Format:
    number_of_vertex
    number_of_edges
    pairs of edges connected (multiple lines)
    0 to end or next graph 
    """   
    num_vertex = int(f.readline())
    if num_vertex == 0:
        return [] 
    num_edges = int(f.readline())
    edgesRead = 0
    adjList = {}
    for x in range(1, num_vertex+1): adjList[x] = [] 
    morelines = True
    while morelines == True:
        vertxList = f.readline().split(' ')
        for i in range(0, len(vertxList)-1 ,2):
            fromVertx = int(vertxList[i])
            toVertx = int(vertxList[i+1])
            addEdge(adjList, fromVertx, toVertx)
            edgesRead += 1
        if edgesRead >= num_edges: morelines = False
    return adjList
    
graphs = []     
f = open("dataCaterpillar.txt")
g = ['dummy']
while g != []: 
    g = readGraph(f);
    if g != []: graphs.append(g)
print(graphs)

i = 0
for graph in graphs:
    if not isConnected(graph): 
        print("Graph", i, "is not connected, not a caterpillar")
    elif not isAcyclic(graph):
        print("Graph", i, "has cycles, not a caterpillar")
    elif not isCaterpillar(graph):
        print("Graph", i, "is not a caterpillar")
    else:
        print("Graph", i, "is a caterpillar !")
    print(findAllPaths(graph,2,2))   
    i = i+1

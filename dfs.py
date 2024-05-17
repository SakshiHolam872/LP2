from collections import defaultdict 
class Graph: 
 def __init__(self): 
  self.graph = defaultdict(list) 
 def addEdge(self, u, v): 
  self.graph[u].append(v) 
 def DFSUtil(self, v, visited): 
  visited.add(v) 
  print(v, end=' ') 
  for neighbour in self.graph[v]: 
   if neighbour not in visited: 
    self.DFSUtil(neighbour, visited) 
 def DFS(self, v): 
  visited = set() 
  self.DFSUtil(v, visited) 
if __name__ == "__main__": 
 g = Graph() 
 g.addEdge(0, 1) 
 g.addEdge(0, 2) 
 g.addEdge(0, 3) 
 g.addEdge(1, 0) 
 g.addEdge(1, 2) 
 g.addEdge(2, 0) 
 g.addEdge(2, 1)
 g.addEdge(2, 4)
 g.addEdge(3, 0) 
 g.addEdge(4, 2)
 print("Following is Depth First Traversal (starting from vertex 0)") 
 # Function call 
 g.DFS(0) 





















 # Algorithm

#Here is a step-by-step explanation of the DFS algorithm:

#1.Choose a starting vertex and mark it as visited.
#2.Visit the vertex and process it.
#3.If there are unvisited neighboring vertices, choose one of them and repeat steps 1 and 2 recursively.
#4.If all neighboring vertices have been visited or there are no neighbors, backtrack to the previous vertex and repeat step 3 if there are remaining unvisited vertices.
#5.Repeat steps 1-4 until all vertices have been visited.
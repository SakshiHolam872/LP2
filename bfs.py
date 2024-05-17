from collections import defaultdict 
class Graph: 
 def __init__(self): 
  self.graph = defaultdict(list) 
 def addEdge(self, u, v): 
  self.graph[u].append(v) 
 def BFS(self, s): 
  visited = [False] * (max(self.graph) + 1) 
  queue = [] 
  queue.append(s) 
  visited[s] = True 
  while queue: 
   s = queue.pop(0) 
   print(s, end=" ") 
   for i in self.graph[s]: 
    if visited[i] == False: 
     queue.append(i) 
     visited[i] = True 
if __name__ == '__main__': 
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

 print("Following is Breadth First Traversal" 
  " (starting from vertex 0)") 
 g.BFS(0)



























 #BFS (Breadth-First Search) is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order. It starts at a given source vertex and visits all of its neighbors before moving on to their neighbors, and so on.

# Here is a step-by-step explanation of the BFS algorithm:

# Initialize an empty queue and an empty set to keep track of visited vertices.
# Enqueue the source vertex into the queue and mark it as visited.
# While the queue is not empty, do the following:
# a. Dequeue a vertex from the queue.
# b. Process the vertex (print it, perform some operation, etc.).
# c. Enqueue all the unvisited neighbors of the vertex and mark them as visited.
# Repeat steps 3 until the queue becomes empty
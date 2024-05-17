import heapq 
def prim_minimum_spanning_tree(graph): 
    minimum_spanning_tree = [] 
    visited = set() 
    start_node = list(graph.keys())[0]   
 
    priority_queue = [(0, start_node, None)]   
    while priority_queue: 
        weight, current_node, parent = heapq.heappop(priority_queue) 
 
        if current_node not in visited: 
            visited.add(current_node) 
            if parent is not None: 
                minimum_spanning_tree.append((parent, current_node, weight)) 
 
            for neighbor, edge_weight in graph[current_node].items(): 
                if neighbor not in visited: 
                    heapq.heappush(priority_queue, (edge_weight, neighbor, current_node)) 
 
    return minimum_spanning_tree 
example_graph = { 
    'A': {'B': 4, 'D': 3, 'E':5}, 
    'B': {'A': 4, 'C': 2,}, 
    'C': {'B': 2, 'D': 1}, 
    'D': {'A': 3, 'C': 1},
    'E': {'A': 5} 
} 
result = prim_minimum_spanning_tree(example_graph) 
print("Minimum Spanning Tree:") 
for edge in result: 
    print(edge )






























# The given code implements Prim's algorithm, not Kruskal's algorithm. Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. Here's a breakdown of the code:

# 1. Initialize some variables:
#    - `INF` is set to a very large value (9999999) to represent infinity.
#    - `V` is the number of vertices in the graph (5 in this case).
#    - `G` is a 2D array representing the adjacency matrix of the graph. Each value `G[i][j]` represents the weight of the edge between vertices `i` and `j`.
#    - `selected` is an array to keep track of the selected vertices in the minimum spanning tree. Initially, all elements are set to 0 (False) to indicate that no vertices are selected yet.
#    - `no_edge` is a counter to keep track of the number of edges in the minimum spanning tree. It is initialized to 0.

# 2. Choose the first vertex (vertex 0) as the starting vertex for the minimum spanning tree and mark it as selected by setting `selected[0]` to True.

# 3. Enter a loop that continues until `no_edge` reaches `V - 1` (the number of vertices minus 1), which is the maximum number of edges in a minimum spanning tree.

# 4. Inside the loop, find the minimum weight edge that connects a vertex in the selected set `S` to a vertex not yet selected.
#    - Initialize `minimum` to `INF` and `x` and `y` to 0.
#    - Iterate over all vertices in the graph.
#      - If the current vertex `i` is selected (`selected[i]` is True), iterate over all vertices `j` in the graph.
#        - If `j` is not selected (`not selected[j]`) and there is an edge between `i` and `j` (`G[i][j] != 0`), then check if the weight of the edge (`G[i][j]`) is less than the current minimum weight.
#          - If it is, update `minimum` with the new minimum weight, and update `x` and `y` with the indices of the vertices that form this minimum weight edge.

# 5. Print the selected edge and its weight.
#    - Print the values of `x`, `y`, and `G[x][y]`, which represent the indices of the vertices and the weight of the edge between them.

# 6. Mark the vertex `y` as selected by setting `selected[y]` to True.

# 7. Increment the `no_edge` counter by 1.

# This process repeats until `no_edge` reaches `V - 1`, meaning that a minimum spanning tree with `V - 1` edges has been found.
#o(ELogV )
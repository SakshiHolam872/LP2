import heapq 
def dijkstra(graph, start): 
    distances = {node: float('infinity') for node in graph} 
    distances[start] = 0 
 
    priority_queue = [(0, start)]  # (distance, node) 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        if current_distance > distances[current_node]: 
            continue 
 
        for neighbor, edge_weight in graph[current_node].items(): 
            distance = current_distance + edge_weight 
 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 
example_graph = { 
    'A': {'B': 1, 'C': 4}, 
    'B': {'A': 1, 'C': 2, 'D': 5}, 
    'C': {'A': 4, 'B': 2, 'D': 1}, 
    'D': {'B': 5, 'C': 1} 
} 
start_node = 'A' 
shortest_distances = dijkstra(example_graph, start_node) 
print("Shortest Distances from", start_node + ":") 
for node, distance in shortest_distances.items(): 
    print(f"To {node}: {distance}")
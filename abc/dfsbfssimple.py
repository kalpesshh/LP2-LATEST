from collections import defaultdict

# Function for DFS traversal
def dfs(graph, start_vertex, visited):
    visited.add(start_vertex)
    print(start_vertex, end=" ")

    for neighbor in graph[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function for BFS traversal
def bfs(graph, start_vertex):
    visited = set()
    queue = []
    queue.append(start_vertex)
    visited.add(start_vertex)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for neighbor in graph[v]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Create a graph
graph = defaultdict(list)

# Take user input for the number of edges and vertices
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Take user input for the edges
print("Enter the edges (format: source destination):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Take user input for the start vertex
start_vertex = int(input("Enter the start vertex: "))

# Perform DFS and BFS traversal
print("DFS Traversal:")
dfs(graph, start_vertex, set())

print("\nBFS Traversal:")
bfs(graph, start_vertex)

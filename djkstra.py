import sys


def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[start] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        min_distance = sys.maxsize
        min_vertex = -1

        # Find the vertex with the minimum distance
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        visited[min_vertex] = True

        # Update the distances of the neighboring vertices
        for v in range(num_vertices):
            if graph[min_vertex][v] > 0 and not visited[v]:
                new_distance = distances[min_vertex] + graph[min_vertex][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances


# Function to get user input for the number of vertices
def get_num_vertices():
    num_vertices = int(input("Enter the number of vertices: "))
    return num_vertices


# Function to get user input for the adjacency matrix
def get_graph(num_vertices):
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    print("Enter the adjacency matrix (enter 0 if there is no edge):")
    for i in range(num_vertices):
        for j in range(num_vertices):
            weight = int(input(f"Enter the weight between vertex {i} and {j}: "))
            graph[i][j] = weight
    return graph


# Function to get user input for the start vertex
def get_start_vertex(num_vertices):
    start_vertex = int(input(f"Enter the start vertex (0 to {num_vertices - 1}): "))
    return start_vertex


# Example usage
num_vertices = get_num_vertices()
graph = get_graph(num_vertices)
start_vertex = get_start_vertex(num_vertices)

distances = dijkstra(graph, start_vertex)

print("Shortest distances from the start vertex:")
for vertex in range(num_vertices):
    print(f"Vertex {vertex}: {distances[vertex]}")

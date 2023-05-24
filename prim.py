def prim(graph):
    # Number of vertices in the graph
    num_vertices = len(graph)

    # Create a list to track the minimum cost of including each vertex in the MST
    min_cost = [float('inf')] * num_vertices

    # Create a list to store the parent vertex of each vertex in the MST
    parent = [None] * num_vertices

    # Create a list to track if a vertex is included in the MST
    in_mst = [False] * num_vertices

    # Choose the first vertex as the starting point
    min_cost[0] = 0

    for _ in range(num_vertices - 1):
        # Find the vertex with the minimum cost that is not yet included in the MST
        min_cost_vertex = None
        for v in range(num_vertices):
            if not in_mst[v] and (min_cost_vertex is None or min_cost[v] < min_cost[min_cost_vertex]):
                min_cost_vertex = v

        # Include the minimum cost vertex in the MST
        in_mst[min_cost_vertex] = True

        # Update the minimum cost and parent for its neighboring vertices
        for v in range(num_vertices):
            if graph[min_cost_vertex][v] != 0 and not in_mst[v] and graph[min_cost_vertex][v] < min_cost[v]:
                min_cost[v] = graph[min_cost_vertex][v]
                parent[v] = min_cost_vertex

    # Print the MST
    print("Minimum Spanning Tree:")
    for v in range(1, num_vertices):
        print(f"{parent[v]} - {v}")


# Function to get user input for the graph
def get_graph_input():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            graph[i][j] = int(input(f"Enter the weight between vertex {i} and {j}: "))

    return graph


# Example usage
graph = get_graph_input()
prim(graph)

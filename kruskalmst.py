def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1


def kruskal(num_vertices, edges):
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    minimum_spanning_tree = []

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        vertex1, vertex2, weight = edge

        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            minimum_spanning_tree.append((vertex1, vertex2, weight))

    return minimum_spanning_tree


# Function to get user input for the number of vertices
def get_num_vertices():
    num_vertices = int(input("Enter the number of vertices: "))
    return num_vertices


# Function to get user input for the edges
def get_edges(num_vertices):
    edges = []
    print("Enter the weight of each edge (or 0 if no edge exists):")
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = int(input(f"Enter the weight between vertex {i} and {j}: "))
            edges.append((i, j, weight))
    return edges


# Example usage
num_vertices = get_num_vertices()
edges = get_edges(num_vertices)
minimum_spanning_tree = kruskal(num_vertices, edges)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    vertex1, vertex2, weight = edge
    print(f"{vertex1} - {vertex2}, Weight: {weight}")

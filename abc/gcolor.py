def is_valid(graph, colors, vertex, color):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True


def graph_coloring(graph, num_colors):
    n = len(graph)
    colors = [-1] * n
    min_colors = float('inf')

    def backtrack(vertex):
        nonlocal min_colors
        if vertex == n:
            min_colors = min(min_colors, max(colors) + 1)
            return

        for color in range(num_colors):
            if is_valid(graph, colors, vertex, color):
                colors[vertex] = color
                backtrack(vertex + 1)
                colors[vertex] = -1

    backtrack(0)
    return min_colors


# Input graph and number of colors from the user
n_vertices = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(n_vertices)]

n_edges = int(input("Enter the number of edges: "))
print("Enter the edges in the format 'u v', where u and v are vertices connected by an edge:")
for _ in range(n_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

num_colors = int(input("Enter the number of colors: "))

min_colors = graph_coloring(graph, num_colors)
print("Minimum number of colors required:", min_colors)

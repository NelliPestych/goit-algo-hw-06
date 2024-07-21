import networkx as nx
from collections import deque

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Алгоритм DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(set(graph[vertex]) - visited)

    return path

# Алгоритм BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return path

# Тестування алгоритмів на графі
graph_dict = nx.to_dict_of_lists(G)

start_node = 'A'
dfs_path = dfs(graph_dict, start_node)
bfs_path = bfs(graph_dict, start_node)

print(f"DFS шлях: {dfs_path}")
print(f"BFS шлях: {bfs_path}")

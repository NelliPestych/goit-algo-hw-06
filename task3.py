import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа з вагами
G = nx.Graph()

# Додавання ваг до ребер
weighted_edges = [
    ('A', 'B', 1), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 3),
    ('C', 'E', 4), ('D', 'E', 1), ('D', 'F', 5), ('E', 'F', 2)
]
G.add_weighted_edges_from(weighted_edges)

# Візуалізація з вагами
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_color='black', font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста з вагами")
plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    path = {node: [] for node in graph.nodes}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                path[neighbor] = path[current_node] + [current_node]

    for node in path:
        path[node].append(node)

    return distances, path

# Знаходження найкоротшого шляху
start_node = 'A'
distances, paths = dijkstra(G, start_node)

print(f"Відстані від вершини {start_node}: {distances}")
print(f"Шляхи від вершини {start_node}: {paths}")

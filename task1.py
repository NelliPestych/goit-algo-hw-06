import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (наприклад, зупинок автобусів)
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Додавання ребер (наприклад, доріг між зупинками)
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')]
G.add_edges_from(edges)

# Візуалізація графа
nx.draw(G, with_labels=True, node_size=700, node_color='skyblue', font_size=15, font_color='black', font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступінь кожної вершини:")
for node in G.nodes():
    print(f"Вершина {node}: {G.degree[node]}")

import networkx as nx
import matplotlib.pyplot as plt

# Grupo Cíclico de ordem 4 (Z/4Z)
G = nx.cycle_graph(4)

# Layout circular para o grafo
pos = nx.circular_layout(G)

# Adicionando rótulos aos nós
labels = {i: f"e^{2 * i * 3.14j / 4}" for i in G.nodes()}

# Desenhando o grafo
nx.draw(G, pos, labels=labels, with_labels=True, node_color='skyblue', node_size=2000)
plt.title('Grafo de Cayley para Z/4Z')
plt.show()
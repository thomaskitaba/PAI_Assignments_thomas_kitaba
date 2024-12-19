import networkx as nx
import matplotlib
matplotlib.use('TkAgg')  # Ensure Matplotlib uses an interactive backend
import matplotlib.pyplot as plt

# Create an empty graph object
G = nx.Graph()

# Add nodes and edges
G.add_node("A")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("D", "B")

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')

# Show the graph
plt.show()

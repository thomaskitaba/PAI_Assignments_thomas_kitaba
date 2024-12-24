#!/usr/bin/python3
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_edge("B", "A",  weight=2)
nx.draw(G, with_labels=True)

pos = nx.spring_layout(G)
# pos = {
#     'A': (0, 0),  # Position for node A
#     'B': (1, 1),  # Position for node B
   
# }

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_weight='bold',  label_pos=0.5)

# plt.margins(1)
plt.show()




















# # Create an empty graph object
# # networkx is used for managing the graph (cities and roads).
# # matplotlib (and pyplot) is used for visualizing the graph as a plot.

# # Define roads (nodes and edges)
# roads = {
#     'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
#     'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
#     'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
#     'Hawassa': [('Addis Ababa', 275)],
#     'Mekelle': [('Gondar', 300)]
# }

# G = nx.Graph()

# # Add nodes and edges
# for city, connections in roads.items():
#     for c in connections:
#         G.add_edge(city, c[0], weight=c[1])

# # Layout options:
# # spring_layout (used in your current code) – Positions nodes based on attractive and repulsive forces, producing a force-directed layout.
# # circular_layout – Positions nodes in a circular arrangement.
# # kamada_kawai_layout – A force-directed layout that aims to preserve the relative distances between nodes.
# # spectral_layout – Positions nodes based on the eigenvectors of the graph's Laplacian matrix.
# # random_layout – Randomly positions nodes in the space.

# # Select a layout:
# pos = nx.spectral_layout(G)  # You can change this to any of the layouts mentioned above

# # Draw the graph with labels and customized styling
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3100, font_size=8, font_weight='bold', width=2)

# # Draw edge labels (distances between cities)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_weight='bold')

# # Display the graph
# plt.margins(0.2)
# plt.show()

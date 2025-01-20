#!/usr/bin/python3
import networkx as nx
import matplotlib
# matplotlib.use('TkAgg')  # Ensure Matplotlib uses an interactive backend
import matplotlib.pyplot as plt

import scipy as sp

# Create an empty graph object
# networkx is used for managing the graph (cities and roads).
# matplotlib (and pyplot) is used for visualizing the graph as a plot.
# Tkinter is the standard GUI library for Python and is required by Matplotlib's TkAgg backend for rendering interactive plots.
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


G = nx.Graph()

# Add nodes and edges
for city, connections in roads.items():
    # print(connections)
    for c in connections:
        G.add_edge(city, c[0], weight=c[1])
        
        
# Position and labels
# Layout options:
# spring_layout (used in your current code) – Positions nodes based on attractive and repulsive forces, producing a force-directed layout.
# circular_layout – Positions nodes in a circular arrangement.
# kamada_kawai_layout – A force-directed layout that aims to preserve the relative distances between nodes.
# spectral_layout – Positions nodes based on the eigenvectors of the graph's Laplacian matrix.
# random_layout – Randomly positions nodes in the space.

# todo: Layout options:
# Choose one of the layouts to avoid a straight-line graph:
# pos = nx.spring_layout(G)  
# pos = nx.circular_layout(G)  
# pos = nx.kamada_kawai_layout(G)  
pos = nx.spectral_layout(G)  
# pos = nx.random_layout(G)  
# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3100, font_size=8, font_weight='bold', width=2)
# Show the graph

edge_labels = nx.get_edge_attributes(G, 'weight')
print
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_weight='bold')

plt.margins(0.2)
plt.show()


#!/usr/bin/env python
"""mapper.py"""

import sys

# Create empty adjency matrix
adjacency_matrix = {}

# Fill adjency matrix
for line in sys.stdin:
  line = line.strip()
  words = line.split(' ')
  node = words[0]
  if node not in adjacency_matrix:
    adjacency_matrix[node] = {}

  # Everything after the key is the neighbors
  neighbors = words[1:]

  for neighbor in neighbors:
    if neighbor not in adjacency_matrix:
      adjacency_matrix[neighbor] = {}
    # Adjency matrix should be set to true for the node and its neighbor
    adjacency_matrix[node][neighbor] = True
    adjacency_matrix[neighbor][node] = True

for node1 in adjacency_matrix:
  for node2 in adjacency_matrix:
    if node1 != node2:
      neighbors_node1 = set(adjacency_matrix[node1])
      neighbors_node2 = set(adjacency_matrix[node2])

      shared_neighbor_nodes = neighbors_node1.intersection(neighbors_node2)
      if len(shared_neighbor_nodes) > 0:
        print('{0} {1} {2}'.format(node1, node2, ' '.join(map(str,shared_neighbor_nodes))))
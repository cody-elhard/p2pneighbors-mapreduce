#!/usr/bin/env python
"""reducer.py"""

import sys

nodes_pair_with_neighbors = {}

for line in sys.stdin:
  line = line.strip()
  words = line.split(' ')

  node1 = words[0]
  node2 = words[1]
  
  new_neighbors = words[2:]

  # IF has not yet been seen set neighbor_nodes to an empty array, which you can append to later
  if (node1, node2) not in nodes_pair_with_neighbors:
    nodes_pair_with_neighbors[(node1, node2)] = []
  
  prev_neighbors = set(nodes_pair_with_neighbors[(node1, node2)])

  nodes_pair_with_neighbors[(node1, node2)] = prev_neighbors.union(set(new_neighbors))

# Finally write out the results
for key, value in nodes_pair_with_neighbors.items():
  print(key, ' '.join(map(str, value)))
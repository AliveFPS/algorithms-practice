"""Calculates shortest path lengths from a root node in a graph using Breadth-First Search (BFS).

Args:
    graph (dict): A dictionary representing the graph, where keys are nodes and 
                    values are lists of their adjacent nodes.
    root: The starting node for the BFS traversal.

Returns:
    dict: A dictionary where keys are nodes in the graph and values are their
            shortest distances from the root node.
"""

from collections import deque


graph = {   'A': ['B', 'C'],
            'B': ['A'],
            'C': ['D'],
            'D': ['E'],
            'E': ['D']}

graphTwo = {'A': ['C'],
            'B': ['C'],
            'C': ['B','H','F','D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C','E'],
            'G': ['H'],
            'H': ['C','G']}


def bfsPathLengths(graph,root):
    path_lengths = {root: 0}
    queue = deque(root)
    visited = [root]

    while queue:
        curr = queue.popleft()

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                path_lengths[neighbor] = path_lengths[curr] + 1

    return path_lengths

print(bfsPathLengths(graph,"A"))
print(bfsPathLengths(graphTwo,"A"))
            



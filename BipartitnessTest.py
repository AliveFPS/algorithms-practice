from collections import deque

graph = {   'A': ['B', 'C'],
            'B': ['A','D'],
            'C': ['A','E'],
            'D': ['B','F'],
            'E': ['C','G'],
            'F': ['D','H'],
            'G': ['E'],
            'H': ['F']
            }

def bipartite(graph, root):
    color = {root: 0}
    visited = []
    queue = deque(root)

    while queue:
        curr = queue.popleft()

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                color[neighbor] = 1 - color[curr]
            elif color[neighbor] == color[curr]:
                return False
            
    return True

print(bipartite(graph,"A"))


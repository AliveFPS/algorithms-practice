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

        for node in graph[curr]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
                path_lengths[node] = path_lengths[curr] + 1

    return path_lengths

print(bfsPathLengths(graphTwo,"A"))
            



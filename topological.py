from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

def topological(graph):
    indegrees = {node: 0 for node in graph}

    for node in graph:
        for neighbour in graph[node]:
            indegrees[neighbour] += 1

    queue = deque([node for node in indegrees if indegrees[node] == 0])

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    
    if len(order) == len(graph):
        return order
    else:
        # Graph has a cycle
        return None
    
print(topological(graph))
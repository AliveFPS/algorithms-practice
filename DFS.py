from collections import deque

graph = {   'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'G'],
            'D': ['F'],
            'E': ['B'],
            'F': ['D'],
            'G': ['C']}

def dfs(graph, root):
    visited = [root]
    stack = deque([root])
    dfsPath = []
    
    while stack:
        node = stack.pop()
        dfsPath.append(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
    
    return dfsPath


print(dfs(graph,"A"))
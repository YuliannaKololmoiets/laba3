from collections import defaultdict, deque

def topological_sort(edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
        if u not in in_degree:
            in_degree[u] = 0

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == len(in_degree):
        return result
    else:
        return -1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

sorted_order = topological_sort(edges)
print( sorted_order)

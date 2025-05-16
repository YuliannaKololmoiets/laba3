from collections import defaultdict

def sorted_edges(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    result = []
    for i in range(1, n + 1):
        neighbors = sorted(graph[i]) if i in graph else []
        result.append(" ".join(map(str, neighbors)))

    return result

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

conections_list = sorted_edges(n, edges)
for line in conections_list:
    print(line)


from collections import defaultdict

def is_complete_graph(n, edges):
    edge_count = defaultdict(set)  # Використовуємо множину для унікальних ребер

    # Заповнюємо словник на основі списку ребер
    for u, v in edges:
        edge_count[u].add(v)
        edge_count[v].add(u)

    # Перевіряємо наявність всіх можливих ребер (включаючи петлі)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and j not in edge_count[i]:
                return "NO"

    return "YES"

# Зчитування кількості графів
k = int(input())

results = []

for _ in range(k):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    results.append(is_complete_graph(n, edges))

print("\n".join(results))

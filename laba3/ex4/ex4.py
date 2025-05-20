from collections import defaultdict

def has_parallel_edges(n, m, edges):
    graph = defaultdict(set)  # ������������� ������� ��� ��������� �����

    for u, v in edges:
        if v in graph[u]:  # ���� ����� ��� �, �� �� ���������� �����
            return "YES"
        graph[u].add(v)

    return "NO"

# ���������� ������� ������
k = int(input())

results = []

for _ in range(k):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    results.append(has_parallel_edges(n, m, edges))

print("\n".join(results))

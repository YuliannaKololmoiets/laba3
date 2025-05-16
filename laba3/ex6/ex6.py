def is_adjacency_matrix(n, matrix):

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return "NO"

    for i in range(n):
        if matrix[i][i] != 0:
            return "NO"

    return "YES"

k = int(input())

results = []

for _ in range(k):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    results.append(is_adjacency_matrix(n, matrix))

print("\n".join(results))


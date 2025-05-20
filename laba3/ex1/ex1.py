def is_tree(matrx):
    n = len(matrx)
    visited = [False] * n
    edge_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if matrx[i][j]:
                edge_count += 1

    if edge_count != n - 1:
        return False

    def dfs(v):
        visited[v] = True
        for u in range(n):
            if matrx[v][u] and not visited[u]:
                dfs(u)

    dfs(0) 

    return all(visited) 

n = int(input())
mayrix = [list(map(int, input().split())) for _ in range(n)]

print("YES" if is_tree(mayrix) else "NO")


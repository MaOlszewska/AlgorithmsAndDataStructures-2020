def DFS_visit(G, u, visited, i):
    visited[u] = True
    for v in range(len(G)):
        if visited[v] == False and G[u][v] == 1:
            DFS_visit(G, v, visited, i)

def breaking(G):
    n = len(G)
    best_vertex = None
    max_count = 0
    for i in range(n):
        visited = [False for _ in range(n)]
        visited[i] = None
        count = 0
        for u in range(n):
            if u != i and visited[u] is False:
                DFS_visit(G,u,visited, i)
                count += 1
            if count > max_count:
                max_count = count
                best_vertex = i
    if max_count == 1:
        return None
    return best_vertex


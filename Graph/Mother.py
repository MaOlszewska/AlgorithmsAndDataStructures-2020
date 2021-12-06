

def DFS(G, v, visited):
    visited[v] = True
    for u in G[v]:
        if visited[u] == False:
            visited[u] = True
            DFS(G, u, visited)

def mother(G):
    visited = [False for _ in range(len(G))]
    for i in range(len(G)):
        if visited[i] == False:
            DFS(G, i, visited)
            mom = i
    visited = [False for _ in range(len(G))]
    DFS(G, mom, visited)
    for i in visited:
        if i == False:
            return False
    return mom

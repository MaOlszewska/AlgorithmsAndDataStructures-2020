def connected(G):
    visited = [False for _ in range(len(G))]
    tab = []
    for v in range(len(G)):
        if visited[v] == False:
            tab.append(DFS_visit(G, v, visited, []))
    return tab

def DFS_visit(G,v,visited, tab):
    visited[v] = visited
    tab.append(v)
    for u in G[v]:
        if visited[u] == False:
            tab = DFS_visit(G, u, visited, tab)
    return tab

G = [[ 1,2],[0,2],[0,1],[4],[3],[7,8],[8],[5,8],[6,7]]

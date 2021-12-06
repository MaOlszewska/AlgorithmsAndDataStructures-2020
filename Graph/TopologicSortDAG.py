def dfs_rec(graph,start,path, visited):
    visited[start] = True
    for edge in graph[start]:
        if edge not in path:
            #print(edge, path)
            dfs_rec(graph, edge,path, visited)
    path.insert(0,start)

def DFS(G):
    path = []
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u] == False:
            dfs_rec(G, u, path, visited)
    print(path)

G = [[1,2,6],[],[3,1],[4,5],[],[],[3]]

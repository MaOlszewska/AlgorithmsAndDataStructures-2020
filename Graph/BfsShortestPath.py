from queue import Queue

def shortestpath(G, s, e):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    path = [None for _ in range(len(G))]
    path[s] = -1
    paths = []
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        v = Q.get()
        if v == e:
            while v != -1:
                paths.insert(0,v)
                v = path[v]
            return paths
        for u in G[v]:
            if visited[u] == False:
                path[u] = v
                Q.put(u)
                visited[u] = True

G = [[2,3,4],[3],[0,3],[0,1,2,4],[0,2]]

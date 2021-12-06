def whichConnected(M, i, j):
    n = len(M)
    neigh = []
    if i * n + 1 + j < n * n:
        neigh.append(i * n + j + 1)
    if i * n - 1 + j >= 0:
        neigh.append(i * n + j - 1)
    if i * n + j - n >= 0:
        neigh.append(i * n + j - n)
    if i * n + j + n <= n*n:
        neigh.append(i * n + j + n)
    return neigh

def deepthOfVertex(M):
    n = len(M)
    D = [0] * n * n
    for i in range(n):
        for j in range(n):
            D[i*n + j] = M[i][j]
    return D

def createGraph(M):
    n = len(M)
    G = [[] for _ in range(n*n)]

    for i in range(n):
        for j in range(n):
            tmp = whichConnected(M, i, j)
            G[i*n + j] = tmp
    return G

def DFS(G, D, t):
    visited = [False] * len(G)
    parent = [-1] * len(G)
    def DFSvisit(G, u):
        visited[u] = True
        for each in G[u]:
            if not visited[each] and D[each] >= t:
                parent[each] = u
                DFSvisit(G, each)

    DFSvisit(G, 0)
    return visited[len(G) - 1]

def app(M, t):
    G = createGraph(M)
    D = deepthOfVertex(M)
    return DFS(G, D, t)

M = [[5,2,1,1],
    [2,1,1,2],
    [3,2,2,2],
    [1,1,1,4]]

print(app(M, 2))
from queue import PriorityQueue
from math import inf

def addCityCenter(G,stores):
    n = len(G)
    print(n)
    newG = [[-1 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(n):
            newG[i][j] = G[i][j]

    for store in stores:
        newG[n][store] = 0
    return newG

def dijkstryMatrix( G, s ):
    def relax(u, v):
        nonlocal Q
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Q.put((D[v],v))
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    processed = [False] * n #tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s], s))
    while not Q.empty():
        _, u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] >= 0 and not processed[v]:
                    relax(u,v)
            processed[u] = True
    return D

def findClosestStore(G, stores):
    G = addCityCenter(G, stores)
    distances = dijkstryMatrix(G, len(G) - 1)
    print(distances)

G = [[-1,3,-1,-1,-1,-1,-1,-1],
    [3,-1,5,2,4,-1,-1,-1],
    [-1,5,-1,6,-1,-1,-1,-1],
    [-1,2,6,-1,1,-1,-1,-1],
    [-1,2,-1,1,-1,1,-1,-1],
    [-1,-1,-1,-1,1,-1,7,-1],
    [-1,-1,-1,2,-1,7,-1,6],
    [-1,-1,-1,-1,-1,-1,6,-1]]

stores = [2,4]

findClosestStore(G, stores)
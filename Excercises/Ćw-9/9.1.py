'''
Proszę zaimplementować algorytm Dijkstry (dla wybranej przez prowadzącego reprezentacji grafu)
'''


'''
Standardowa dijkstra.
'''
from queue import PriorityQueue

def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t


def printsolution(distance, parent,s):
    for i in range(1, len(distance)):
        print(s,"->",i,distance[i])
        print(printpath(parent, i,[]))


def dijkstra(G, s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i],i))

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != 0:
                    if distance[v] + G[v][u] < distance[u]: # relaksacja
                        distance[u] = distance[v] + G[v][u]
                        pq.put((distance[u],u))
                        parent[u] = v
            visited[v] = True
    printsolution(distance, parent,s)
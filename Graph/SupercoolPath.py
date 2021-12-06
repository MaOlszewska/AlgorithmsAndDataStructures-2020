from queue import PriorityQueue
from math import inf

def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t

def dijkstra(G, s):
    n = len(G)
    distance = [inf for _ in range(n)]
    lenght = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0
    lenght[s] = 0

    for i in range(n):
        pq.put((distance[i],lenght[i], i))

    while not pq.empty():
        _, _,  v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != 0:
                    if distance[v] + G[v][u] == distance[u] and lenght[v] + 1 < lenght[u]:
                        lenght[u] = lenght[v] + 1
                        parent[u] = v

                    if distance[v] + G[v][u] < distance[u]:
                        lenght[u] = lenght[v] + 1
                        distance[u] = distance[v] + G[v][u]
                        pq.put((distance[u],lenght[u], u))
                        parent[u] = v
            visited[v] = True
    return distance, parent


def printsolution(distance, parent, s):
    for i in range(1, len(distance)):
        print(s,"->",i,distance[i])
        print(printpath(parent, i,[]))

G = [[0,1,3,3,0,10,0],
     [1,0,1,1,3,0,0],
     [3,1,0,0,2,0,0],
     [3,1,0,0,0,3,4],
     [0,3,2,0,0,4,1],
     [10,0,0,3,4,0,0],
     [0,0,0,4,1,0,0]]

d, p = dijkstra(G,0)
printsolution(d,p,0)


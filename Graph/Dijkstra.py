from queue import PriorityQueue
from math import inf
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
    distance = [inf for _ in range(n)]
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
                    if distance[v] + G[v][u] < distance[u]:
                        distance[u] = distance[v] + G[v][u]
                        pq.put((distance[u],u))
                        parent[u] = v
            visited[v] = True
    printsolution(distance, parent,s)


def dijkstra1(G, s, t):  # między podanymi wierzchołkami
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    pq = PriorityQueue()
    distance[s] = 1

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, v = pq.get()
        if v == t:
            printsolution(distance, parent, s)
            return parent, distance[t]
        for u in range(n):
            if G[v][u] != 0 and visited[u] == False:
                if distance[v] * G[v][u] < distance[u]:
                    distance[u] = distance[v] * G[v][u]
                    parent[u] = v
                    pq.put((distance[u], u))
    printsolution(distance, parent ,s)

if __name__ == '__main__':
    G1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    G = [[0, 1, 5, 0, 0],
         [1, 0, 2, 7, 8],
         [5, 2, 0, 0, 3],
         [0, 7, 0, 0, 1],
         [0, 8, 3, 1, 0]]
    dijkstra(G,0)



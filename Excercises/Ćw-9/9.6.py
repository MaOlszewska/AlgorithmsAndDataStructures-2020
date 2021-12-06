'''
Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie (bez
implementacji)
'''

'''
Uzywamy standardowej dijkstry z tym, że zamieniamy w relaksjacji wartości na logarytmy, dzięki czemu będzie mogli dodawać
a nie mnożyć klejnych liczb i bedzięmy pracować na owiele mniejszych liczbach.
'''

from queue import PriorityQueue
from math import inf, log10


def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t

def printsolution(distance, parent, s):
    for i in range(1, len(distance)):
        print(s, "->", i, distance[i])
        print(printpath(parent, i,[]))

def dijkstra(G, s):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i], i))

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != 0:
                    if distance[v] + log10(G[v][u]) < distance[u]:
                        distance[u] = distance[v] + log10(G[v][u])
                        pq.put((distance[u],u))
                        parent[u] = v
            visited[v] = True
    printsolution(distance, parent,s)

G = [[0, 10, 100, 0, 0],
         [10, 0, 100, 10, 100],
         [100, 100, 0, 0, 1000],
         [0, 10, 0, 0, 10],
         [0, 100, 1000, 10, 0]]
dijkstra(G, 0)

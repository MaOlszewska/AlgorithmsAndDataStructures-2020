'''
Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.
'''

from queue import PriorityQueue
from math import inf

def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t

def printsolution(distance, parent,s,t):
    print(s,"->",t , distance[t])
    print(printpath(parent, t,[]))


def dijkstra1(G, s, t):  # między podanymi wierzchołkami
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i], i))
    while not pq.empty():
        d, v = pq.get()
        if v == t:
            printsolution(distance, parent, s, t)
            return parent, distance[t]
        for u in range(n):
            if G[v][u] != 0 and visited[u] == False:
                if distance[v] * G[v][u] < distance[u]:
                    distance[u] = distance[v] + G[v][u]
                    parent[u] = v
                    pq.put((distance[u], u))
    printsolution(distance, parent ,s, t)

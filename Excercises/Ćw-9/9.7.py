'''
Przewodnik chce przewieźć grupę K turystów z
miasta A do miasta B. Po drodze jest jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o
różnej pojemności. Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów.
Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
(najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
dostali się z A do B.
'''

'''
Kilka rozwiązań:
1-Maksymalne drzewo rozpinające- najmniejsza wartośc krawędzi to szukana liczba 
2-Dijksta z tym, że używamy kolejki w odwrotnej kolejności (mnożymy przez  -1)
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

def printsolution(distance, parent,s):
    for i in range(1, len(distance)):
        print(s, "->", i, distance[i])
        print(printpath(parent, i,[]))

def dijkstra(G, s):
    n = -1
    for i in range(len(G)):
       n = max(n, G[i][1], G[i][0])
    n += 1
    new_G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(G)):
        new_G[G[i][0]][G[i][1]] = G[i][2]
        new_G[G[i][1]][G[i][0]] = G[i][2]
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = inf


    pq.put((-1 * distance[s], s))

    while not pq.empty():
        _, u = pq.get()
        if not visited[u]:
            for v in range(n):
                if new_G[u][v] != 0 and not visited[v]:
                    if distance[v] > min(distance[u], new_G[u][v]):
                        distance[v] = min(distance[u], new_G[u][v])
                        pq.put((-1 * min(distance[u], new_G[u][v]), v))
                        parent[v] = u
            visited[u] = True
    printsolution(distance, parent, s)
G = [(0, 1, 15), (0, 2, 7), (0, 3, 12), (1, 5, 8), (5, 6, 9), (3, 5, 10), (3, 4, 11), (4, 6, 15), (2, 4, 9)]
dijkstra(G, 0)

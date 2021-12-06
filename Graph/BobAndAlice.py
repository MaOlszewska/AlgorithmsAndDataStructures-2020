''' Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
1jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
poprawny).'''

from queue import PriorityQueue
from math import inf


def dijkstryMatrix(G, s, IsItAlicia):
    def relax(u, v):
        nonlocal Q
        if iteration[u]:
            dist = G[u][v]
        else:
            dist = 0

        if D[v] > D[u] + dist:
            iteration[v] = not iteration[u]
            D[v] = D[u] + dist
            Q.put((D[v], v))
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    iteration = [None] * n
    processed = [False] * n  # tablica przetworzonych wierzchołków
    if IsItAlicia:
        iteration[s] = True
    else:
        iteration[s] = False
    D[s] = 0
    Q.put((D[s], s))
    while not Q.empty():
        _, u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u, v)
            processed[u] = True

    return D


def tripin(G, s, t):
    AlicjaTrip = dijkstryMatrix(G, s, True)
    BobTrip = dijkstryMatrix(G, s, False)
    return min(AlicjaTrip[t], BobTrip[t])


G = [[-1, 4, 3, 3, -1],
     [4, -1, 7, -1, -1],
     [3, 7, -1, 4, 2],
     [3, -1, 4, -1, 5],
     [-1, -1, 2, 5, -1]]

G = [[-1, 2, -1, -1, -1, -1, -1, -1, 5],
     [-1, -1, 1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, 3, -1, -1, 1, -1, -1],
     [-1, -1, -1, -1, 1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, 4, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
     [-1, -1, -1, -1, -1, 1, -1, -1, -1],
     [-1, -1, -1, -1, -1, -1, 1, -1, -1],
     [-1, -1, -1, -1, -1, -1, -1, 4, -1]]

print(tripin(G, 0, 5))
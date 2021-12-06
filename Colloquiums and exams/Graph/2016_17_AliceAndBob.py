'''
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo.
'''

from queue import PriorityQueue


def dijkstra(G, s, driver):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0

    who_drive = [None for _ in range(len(G))]

    if driver is True:
        who_drive[s] = True
    else:
        who_drive[s] = False

    pq.put((distance[s],s))

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != -1:
                    if who_drive[v]:
                        dist = G[u][v]
                    else:
                        dist = 0
                    if distance[v] + dist < distance[u]:
                        distance[u] = distance[v] + dist
                        pq.put((distance[u],u))
                        parent[u] = v
                        who_drive[u] = not who_drive[v]
            visited[v] = True
    return distance

def AliceAndBob(G, x, y):
    Alice = dijkstra(G, x, True)
    Bob = dijkstra(G, x, False)

    if Bob[y] > Alice[y]:
        return 'ALice', Alice[y]
    else:
        return 'Bob', Bob[y]

G = [[-1, 4, 1, 3, -1],
     [4, -1, 7, -1, -1],
     [1, 7, -1, 4, 2],
     [3, -1, 4, -1, 5],
     [-1, -1, 2, 5, -1]]

print(AliceAndBob(G, 0,4))

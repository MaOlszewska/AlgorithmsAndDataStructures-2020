'''
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to
miasta a krawędzie to drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach
jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za
kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy.
Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak najszybszy (ale przede wszystkim
poprawny).
'''

'''
wykonujemy dwa ray algorytm dijkstry z tym, że raz uwzględniamy to, że Alicja zaczyna, a drugi raz to, że Bob.
Tworzymy tablice w której zapisjemy czy teraz kolej alicji czy nie, jesli tak to dodajmy noramnie wge do sumy, jesli nie to dodajemy 0.
Wybiermay to rozwiaznie gdzi suma jest mniejsza.
'''


from queue import PriorityQueue
from math import inf


def dijkstra(G, s, driver):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0
    who_drive = [0 for _ in range(len(G))]
    pq.put((distance[s], s))
    if driver is True: # ALICJA
        who_drive[s] = True
    else:  # BOB
        who_drive[s] = False

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != -1:
                    if who_drive[v] is True:
                        drive = G[v][u]
                    else:
                        drive = 0

                    if distance[v] + drive < distance[u]:
                        who_drive[u] = not who_drive[v]
                        distance[u] = distance[v] + drive
                        pq.put((distance[u],u))
                        parent[u] = v
            visited[v] = True
    print(distance)
    return distance, parent


def printpath(parent, i, t ):
    if parent[i] == -1:
        t.append(i)
        return t
    t = printpath(parent, parent[i], t)
    t.append(i)
    return t

def printsolution(distance, parent,s, e):
        print(s,"->",e,distance[e])
        print(printpath(parent, e,[]))


def fast_and_furious(G, x, y):
    Alice, parent_alice= dijkstra(G, x, True)
    Bob, parent_bob = dijkstra(G, x, False)
    if Alice[y] < Bob[y]:
        printsolution(Alice, parent_alice, x, y)
        return Alice[y]
    else:
        printsolution(Bob, parent_bob, x, y)
        return Bob[y]


G = [[-1, 4, 3, 3, -1],
     [4, -1, 7, -1, -1],
     [3, 7, -1, 4, 2],
     [3, -1, 4, -1, 5],
     [-1, -1, 2, 5, -1]]

G1 = [[-1,2,-1,-1,-1,-1,-1,-1,5],
    [-1,-1,1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,3,-1,-1,1,-1,-1],
    [-1,-1,-1,-1,1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,4,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,4,-1]]
print(fast_and_furious(G1, 0, 6))
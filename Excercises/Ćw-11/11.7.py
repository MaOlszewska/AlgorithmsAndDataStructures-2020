'''
Dany jest graf skierowany G = (V, E) oraz wierzchołki s i t. Proszę
zaproponować algorytm znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.
'''

'''
Każdy z wierzchołków rozdzielamy na dwa, z jednym łączymy wsyztskie krawędzie wchodzące, a z drugim wsytskie które wychodzą 
 z tego wierzchołka. Dwa nowe wierzchołki łączymy jedną krawędzią, zgodnie z kierunkiem. Wszystkim krawędziom przypisujemy wagę 1.
Wywołujemy algorytm wyznaczający maksymalny przepływ w grafie miedzy wierzhcołkami s i t. Znaleziona wartość przepływu bedzie liczbą
rozłącznych scieżek, bo mamy pewność, że przez jeden wierzchołek przepłynie tylko jedna jednostka przepływu.
'''


from queue import Queue

def BFS(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    distance = [-1] * len(G)

    visited[s] = True
    distance[s] = 0

    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)

    return visited[t]

# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(G, s, t):
    n = len(G)
    parents = [None] * n
    flow = 0

    while BFS(G, s, t, parents):
        # szukamy krawędzi o najmniejszej pojemności rezydualnej (czyli
        # największego przepływu jaki może być na danej ścieżce)
        # idziemy od ujścia po parentach w górę
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parents[current]][current] < cur_flow:
                cur_flow = G[parents[current]][current]
            current = parents[current]

        # po przejściu ścieżki zwiększamy flow o najmniejszą pojemność
        # rezydualną na tej ścieżce (cur_flow)
        flow += cur_flow

        # aktualizujemy pojemności rezydualne istniejących krawędzi oraz
        # krawędzi powrotnych, znowu idziemy od ujścia po parentach w górę
        v = t

        while (v != s):
            G[parents[v]][v] -= cur_flow
            G[v][parents[v]] += cur_flow
            v = parents[v]
    # g.printG()
    return flow


def newVertixInGraph(G):
    n = len(G)
    newG = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

    for u in range(n):
        for v in range(n):
            newG[n + u][v] = G[u][v]  # przepinamy krawedzie wychodzace z G
            newG[u][v] = 0  # usuwamy krawedzie wychodzace z g
        newG[u][n + u] = 1  # podpinamy G do newG
    return newG


def numberOfDisjointPaths(G, s, t):
    G = newVertixInGraph(G)
    for u in range(len(G)):
        if G[s][u] == 1:
            G[s][u] = float('inf')
    return Ford_Fulkerson(G, s, t)


G = [[0, 1, 1, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 0]]

print(numberOfDisjointPaths(G, 0, 3))
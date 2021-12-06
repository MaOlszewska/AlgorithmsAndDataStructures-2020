'''szukanie cyklu w grafie o minimalnej wadze'''
'''Dla każdej krawędzi, którą tymczasowo usuwam z grafu, wywołuje dijkstre, która obliczy długość ścieżki między tymi
krawędziami, póżniej dodaje wagę tej usuniętej krawędzi, która razem z tą scieżką tworzy cykl, jeśli taka ścieżka
w ogóle istnieje, odpowiedzią jest minimum z wszystkich znalezionych tak cykli'''


from queue import PriorityQueue

def dijkstra(G, s, t):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
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
            return parent, distance[t]
        for u in range(n):
            if G[v][u] != -1 and visited[u] == False:
                if distance[v] + G[v][u] < distance[u]:
                    distance[u] = distance[v] + G[v][u]
                    parent[u] = v
                    pq.put((distance[u], u))
        visited[v] = True
    return parent, distance[t]

def printpath(parent, i, cycle):
    if parent[i] == -1:
        cycle.append(i)
        return cycle
    cycle = printpath(parent, parent[i], cycle)
    cycle.append(i)
    return cycle

def min_cycle(G):
    minw = float('inf')
    cycle = []
    for u in range(len(G)):
        for v in range(u, len(G)):
            if G[u][v] != -1:
                weight = G[u][v]

                # usuwamy rozwazana krawedz
                G[u][v] = -1
                G[v][u] = -1
                P, d = dijkstra(G, u, v)
                d += weight
                G[u][v] = weight
                G[v][u] = weight

                if d == float('inf'):
                    continue
                if d < minw:
                    minw = d
                    cycle = printpath(P, v, [])
    return cycle

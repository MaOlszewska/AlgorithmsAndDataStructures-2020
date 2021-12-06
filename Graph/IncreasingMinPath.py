'''Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).'''

'''WYkonujemy algorytm dijkstry,w którym sortujemy krawędzie malejąco'''

def relax(u, v, w, parents, distance):
    if distance[u] > distance[v] + w:
        distance[u] = distance[v] + w
        parents[u] = v

def minimal_increasing_paths(G, s, t):
    n = len(G)
    edges = []
    for v in range(n):
        for u in range( n):
            if G[v][u] != 0:
                edges.append((v, u, G[v][u]))
    sorted_edges = sorted(edges, key = lambda x : x[2], reverse = True)

    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    parents = [-1 for _ in range(n) ]

    for edge in sorted_edges:
        relax(edge[0], edge[1], edge[2], parents, distance)

    path = []
    d = None
    if distance[t] != float("inf"):
        d = distance[t]
        while t != -1:
            path.insert(0,t)
            t = parents[t]
    return path, d

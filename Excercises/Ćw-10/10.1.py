'''
Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).
'''

'''
Tworzymy trzy-elementowe krotki, które będą zawierać wierzchołki, które łączą daną krawędz i wagę tej krawędzi.
Sortujemy krawędzie po wagach w kolejności malejącej.
Póżniej wykonujemy relaksacje na kraedziach w takiej kolejności.
'''
from math import inf

def relax(u, v, w, parents, distance):
    if distance[u] > distance[v] + w:
        distance[u] = distance[v] + w
        parents[u] = v

def increasing_path(G,x,y):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[x] = 0
    edges = []
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != 0:
                edges.append((i,j,G[i][j]))
    sorted_edges = sorted(edges, key = lambda x: x[2], reverse = True)

    for edge in sorted_edges:
        relax(edge[0], edge[1], edge[2], parent, distance)

    path = []
    if distance[y] != inf:
        while y != -1:
            path.append(y)
            y = parent[y]
    return path, distance[y]

G = [[0, 10, 11, 0, 0, 0, 0, 0],
    [10, 0, 0, 9, 0, 0, 0, 0],
    [11, 0, 0, 8, 0, 0, 0, 0],
    [0, 9, 8, 0, 7, 1,7, 0],
    [0, 0, 0, 7, 0, 0, 0, 11],
    [0, 0, 0, 1, 0, 0, 0, 11],
    [0, 0, 0, 7, 0, 0, 0, 11],
    [0, 0, 0, 0, 11, 11, 11, 0]]
print(increasing_path(G, 0,7))
'''
. Proszę zaimplementować wybrany przez siebie algorytm obliczania minimalnego drzewa rozpinającego
dla wybranej przez prowadzącego reprezentacji grafu
'''

# KRUSKAL

'''
Tworzymy zbiór krawędzi oraz liste L uporządkowaną względem wag.
Dopóki w T nie am wszytskich wierzchoolków, wybieramy z L krawędz i jeśli ona nie tworzy
cyklu z obecnymi w T krawędziami to dodajemy ją tam.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x is not x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return 1
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def kruskal(G):
    n = len(G)
    edges = []
    t = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                t.append((G[i][j], i, j))
    t.sort(key = lambda t: t[0])

    for i in range(n):
        edges.append(Node(i))

    A = []
    weight = 0
    for edge in range(n):
        v = edges[t[edge][1]]
        u = edges[t[edge][2]]
        if not find(v) is find(u): # czy v i u leżą w innych składowych grafu
            union(v, u) # łaczymy zbiory
            A.append((v.val, u.val))
            weight += t[edge][0]
    return weight, A


# PRIM

from queue import PriorityQueue

def prim(G, v):
    Q = PriorityQueue()  # umiszczenie wszytskich wierzchołkó w kolejce z wagą inf
    for i in range(len(G)):
        Q.put((float('inf'), i))
    W = [float('inf')] * len(G)

    Q.put((0, v))   # dla startowego ustawmaiy wage na zero , bo od niego zaczniemy
    W[v] = 0
    parent = [None] * len(G)

    processed = [False] * len(G)  # tablica przetworzonych wierzchołków

    while Q.qsize(): # póki są wierzchołki w kolejce to wyjmujemy ten o najmneijszej wadze
        _, t = Q.get()
        for u in range(len(G)):
            if G[t][u] != 0 and not processed[u] and G[t][u] < W[u]:
                W[u] = G[t][u]   # sprawdzamy dla każdej krawedzi czy waga jest mniejsza niz waga u w kolejce(osobna tablica z wagami)
                parent[u] = t # to zamieniamy te wagi i dodajemy ten wierzchołek do kolejki z nową wagą i ustawiamy parenta
                Q.put((W[u], u))
        processed[t] = True   # oznaczamy wierzchołek jako sprocesowany

    for i in range(len(parent)):
        if parent[i] is not None:
            print(i, " -> ", parent[i])
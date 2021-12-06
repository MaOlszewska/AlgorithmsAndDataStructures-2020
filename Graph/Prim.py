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

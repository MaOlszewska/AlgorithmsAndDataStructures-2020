###V1 O(v^3)
'''Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci macierzowej
(domknięcie przechodnie grafu G, to graf nad tym
samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma krawędź z u do v wtedy i
tylko wtedy, gdy w G istnieje ścieżka z u do v.'''

def floydWarshal(G):
    S = [[False for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):   # w tablicy wynikowej tam gdzie jest krawędz zaznaczam True jęsli nie ma krawędzi to False
            if G[i][j] != 0:
                S[i][j] = True

    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = S[u][w] or (S[u][v] and S[v][w])   # jesli z u do w można przejść przez wierzchołek v to zncazy ze można stworzyć kraedz łączącą u i w więć zaznaczamy true
    return S

def closure(G):
    H = floydWarshal(G)
    for i in range(len(H)):
        for j in range(len(H)):
            if H[i][j]:
                H[i][j] = 1
            else:
                H[i][j] = 0
    return H

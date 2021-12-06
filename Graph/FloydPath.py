def reconstruction(P, s,t):
    path = [t]
    v = P[s][t]
    while v != -1:
        path.append(v)
        v = P[s][v]
    return path[::-1]

def floydWarshal(G):
    P = [[ -1 for _ in range(len(G))] for _ in range(len(G))]
    S = [[float('inf') for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):  # Tablica dynamiczna z kosztami przejsc dla każdej pary wierzchołków
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
                P[i][j] = i
            if i == j:
                S[i][j] = 0

    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                if  S[u][w] > S[u][v] + S[v][w]:
                    S[u][w] = S[u][v] + S[v][w] # jesli koszt z u, w jest mniejszy niż koszt
                    P[u][w] = P[v][w]
    for each in S:   # z u do v i z v do w to aktualizujemy tablice
        print(each)
    print(P)
    print(reconstruction(P,4,3))

G = [
    [0, 5, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [7, 0, 0, 1, 0],
    [0, 0, 0, 0, 2],
    [0, 2, 2, 0, 0],
]

floydWarshal(G)
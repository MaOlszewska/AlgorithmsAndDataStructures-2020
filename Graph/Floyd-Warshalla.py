def floydWarshal(G):
    S = [[float('inf') for _ in range(len(G))] for _ in range(len(G))]
    for i in range(len(G)):  # Tablica dynamiczna z kosztami przejsc dla każdej pary wierzchołków
        for j in range(len(G)):
            if G[i][j] != 0:
                S[i][j] = G[i][j]
            if i == j:
                S[i][j] = 0

    for each in S:
        print(each)
    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])  # jesli koszt z u, w jest mniejszy niż koszt

    for each in S:   # z u do v i z v do w to aktualizujemy tablice
        print(each)


G4 = [
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0],
      [1, 1, 1, 0, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 1, 1],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
     ]
G3 = [
      [0, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 0],
     ]
floydWarshal(G3)
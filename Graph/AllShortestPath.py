def FloydWarshal(G):
    S = [[float('inf') for i in range(len(G))] for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != -1:
                S[i][j] = G[i][j]
            if i == j:
                S[i][j] = 0

    for v in range(len(G)):
        for u in range(len(G)):
            for w in range(len(G)):
                S[u][w] = min(S[u][w], S[u][v] + S[v][w])
    return S


def howManyShortestPaths(G, S, s, t):
    counter = 0
    for v in range(len(G)):
        if S[s][t] == S[s][v] + S[v][t] and v != s and v != t:
            counter = counter + 1 + howManyShortestPaths(G, S, s, v)
    return counter


def app(G, s, t):
    return howManyShortestPaths(G, FloydWarshal(G), s, t)


G = [[-1, 1, 1, 2, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, -1, 1, 2],
     [-1, -1, -1, -1, 1],
     [-1, -1, -1, -1, -1]]

print(app(G, 0, 4))
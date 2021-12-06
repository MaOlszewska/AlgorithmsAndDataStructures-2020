'''Nie działa'''

def listToMatrixG(G, L):
    n = len(L)
    Matrix = [[0 for _ in range(n)] for _ in range(n)]
    for edge in G:
        Matrix[edge[0]][edge[1]] = edge[2]
        Matrix[edge[1]][edge[0]] = edge[2]
    return Matrix


def relax(G, u, v, parent, distance):
    if distance[v] > distance[u] + G[u][v]:
        distance[v] = distance[u] + G[u][v]
        parent[v] = u


def word(G, w="tot"):
    L, E = G
    n = len(L)
    G = listToMatrixG(E, L)
    whereIsIT = [[] for _ in range(len(w))]
    for litera in range(len(w)):
        for i in range(len(L)):
            if L[i] == w[litera]:
                whereIsIT[litera].append(i)

    parent = [-1] * n
    distance = [float('inf')] * n
    for each in whereIsIT[0]:
        distance[each] = 0
        break

    for iteracja in range(len(w) - 1):
        for poczatek in whereIsIT[iteracja]:
            for v in range(n):
                if L[v] == w[iteracja + 1] and G[poczatek][v] != 0:
                    relax(G, poczatek, v, parent, distance)
    print(distance)
    minLen = float('inf')
    idOfMinLen = -1
    for each in whereIsIT[len(w) - 1]:
        if distance[each] < minLen:
            minLen = distance[each]
            idOfMinLen = each
    print(minLen, distance)
    if minLen == float('inf'):
        return -1

    path = []
    while idOfMinLen != -1:
        path.append(idOfMinLen)
        idOfMinLen = parent[idOfMinLen]
    return(path[::-1], minLen)


L = ["k", "k", "o", "o", "t", "t"]
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)

print(word(G))
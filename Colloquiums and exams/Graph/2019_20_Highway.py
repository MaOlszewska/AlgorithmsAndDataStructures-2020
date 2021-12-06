'''
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad,
tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =√(x1 − x2)^2 + (y1 − y2)^2.
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonejw km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni
dzielącą otwarcie pierwszej i ostatniej autostrady
'''

def distanceBetween(x1, y1, x2, y2):
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)


def createGraph(Points):
    n = len(Points)
    G = [[0 for i in range(n)] for i in range(n)]

    for u in range(n):
        for v in range(n):
            if u != v:
                G[u][v] = ceil(distanceBetween(Points[u][0], Points[u][1], Points[v][0], Points[v][1]))
                G[v][u] = ceil(distanceBetween(Points[u][0], Points[u][1], Points[v][0], Points[v][1]))
    return G


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


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


def kruskal(G, u, v):
    n = len(G)
    edges = []
    for i in range(n):
        for j in range(i, n):
            if G[i][j] != 0:
                edges.append((abs(G[i][j] - G[u][v]), i, j))

    edges.sort(key=lambda edges: edges[0])

    sets = []
    for i in range(n):
        sets.append(Node(i))

    A = []
    weight = 0
    for edge in range(1, n):
        v = sets[edges[edge][1]]
        u = sets[edges[edge][2]]
        if not find(v) is find(u):  # czy v i u leżą w innych składowych grafu
            union(v, u)  # łaczymy zbiory
            A.append((v.val, u.val))
            weight += edges[edge][0]

    minVal = inf
    maxVal = -1 * inf
    for each in A:
        maxVal = max(G[each[0]][each[1]], maxVal)
        minVal = min(G[each[0]][each[1]], minVal)
    return abs(maxVal - minVal)


def highway(A):
    G = createGraph(A)
    n = len(G)

    minOfDifference = float('inf')
    for u in range(n):
        for v in range(u, n):
            minOfDifference = min(kruskal(G, u, v), minOfDifference)
    return minOfDifference
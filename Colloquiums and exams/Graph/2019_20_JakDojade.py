'''
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego,
który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P.
Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
'''

from queue import PriorityQueue


def createPath(G, P, d, s, t):
    _, p = jak_dojade(G, P, d, s, t)
    path = []
    curr = t
    while curr != s:
        if curr == -1:
            return None
        path.append(curr)
        curr = p[curr]
    path.append(s)
    return path[::-1]

def jak_dojade(G, P, d, a, b):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[a] = 0
    Fuel = [0 for _ in range(n)]
    Fuel[a] = d
    pq.put((distance[a], a))

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != -1 and G[v][u] >= Fuel[u]:
                    if distance[v] + G[v][u] < distance[u]:
                        distance[u] = distance[v] + G[v][u]
                        pq.put((distance[u], u))
                        parent[u] = v
                        if u in P:
                            Fuel[u] = d
                        else:
                            Fuel[u] -= G[v][u]
            visited[v] = True
    return distance,parent

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
print(createPath(G,P,5,0,2))
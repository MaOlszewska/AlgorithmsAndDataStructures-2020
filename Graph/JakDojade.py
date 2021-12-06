'''Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak
krawędzi). W niektórych wierzchołkach są stacje paliw, podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany do pełna.
Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej
trasy od wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych
na trasie wierzchołków (zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej
odległość d bez tankowania).
'''

# Wykonujemy zmodyfikowany algorytm Dijkstry. Tworzymy tablice z paliwem, w której oznaczamy ile mamy paliwa chcąc wjechać
# w jakiś wierzchołek. Żeby wjechać do jakiegoś wierzchołka to musimy sprawdzić czy nam wystarczy paliwa, jeśli nie to
# pomijamy. Jeżeli odległość do wierzchołka jest  mniejsza albo równa aktualnej ilosci paliwa, to wjeżdzamy do miasta
# i relaksujemy się. Sprawdzamy czy wierzchołek do którego wjehcaliśmy ejst stacją jeśli tak to tankujemy do pełna.
# jesli nie to odejmujmy od akutalnej ilości paliwa tyli ile wykorzystalismy na podróż. Póżniej odtwarzamy ścieżke do
# docelowego maista, jeśli rodzicem docelowe miasta jest -1 to zwaracamy none.

from queue import PriorityQueue

def jak_dojade(G, stacje, d, s, t):
    n = len(G)
    D = [float('inf')] * n
    D[s] = 0
    fuelLeft = [0] * n
    fuelLeft[s] = d
    Parent = [-1] * n
    Q = PriorityQueue()
    Q.put((D[s], s))

    while not Q.empty():
        _, u = Q.get()
        for v in range(n):
            if G[u][v] != -1  and G[u][v] <= fuelLeft[u]:
                if D[v] >= D[u] + G[u][v]:
                    D[v] = D[u] + G[u][v]
                    if v in stacje:
                        fuelLeft[v] = d
                    else:
                        fuelLeft[v] = fuelLeft[u] - G[u][v]
                    Q.put((D[v], v))
                    Parent[v] = u
    return D, Parent


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



G = [[-1, 1, 1, 2, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, -1, 1, 1],
     [-1, -1, -1, -1, 1],
     [-1, -1, -1, -1, -1]]

P = [0, 1, 3]

G1 = [[-1,1,-1,2,5,-1,-1],
     [-1,-1,2,-1,2,-1,-1],
     [-1,-1,-1,-1,-1,-1,3],
     [-1,-1,-1,-1,-1,2,-1],
     [-1,-1,-1,3,-1,-1,5],
     [-1,-1,-1,-1,-1,-1,5],
     [-1,-1,-1,-1,-1,-1,-1]]

print(createPath(G, P, 6, 0, 2))
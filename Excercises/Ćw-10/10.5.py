'''
Dana jest tabela kursów walut. Dla każdych dwóch walut x oraz y wpis
K[x][y] oznacza ile trzeba zapłacić waluty x żeby otrzymać jednostkę waluty y.
Proszę zaproponować algorytm, który sprawdza czy istnieje taka waluta z,
że za jednostkę z można uzyskać więcej niż jednostkę z
przez serię wymian walut.
'''

'Przechodzę na logarytmy i sprawdzam czy istnieje cykl ujemny, jeśli isteniej to oznacza, że można uzyskać więcej' \
'przez wymianę'

from math import log2

def bellmanFord(G, s):
    distance = [float('inf')] * len(G)
    parent = [None] * len(G)
    distance[s] = 0

    # relaksacja
    for i in range(len(G) - 1):
        for u in range(len(G)):
            for v in range(len(G)):
                if G[u][v] != 0:
                    if distance[v] > distance[u] + G[u][v]:
                        distance[v] = distance[u] + G[u][v]
                        parent[v] = u
    # weryfikacja
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] != 0 and distance[v] > distance[u] + G[u][v]:
                return True
    return False


def currencyExchange(G, z):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                G[u][v] = log2(G[u][v])

    return bellmanFord(G, z)
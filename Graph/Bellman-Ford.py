def relax(u, v, distance, parent):
    if distance[v] > distance[u] + G[u][v]:
        distance[v] = distance[u] + G[u][v]
        parent[v] = u

def bellman_Ford(G, s):
    distance = [float('inf')] * len(G)  #  dla każdego wierzchołka dystans wynosi inf tylko dla startowego zero
    parent = [None] * len(G)
    distance[s] = 0

    # relaksacja
    for i in range(len(G) - 1):  # kązdy obied ustala koszto dojścia do przynajmniej jednego wiezchołka dlatego musimy wykonac go dla n-1 wierzchołków, ponieważ wierzchołek starrtowy ma zero
        for u in range(len(G)):   # dla każdej krawędzi wykonujemy relaksajce i powtarzamy to E -1  razy
            for v in range(len(G)):
                if G[u][v] != 0:
                    relax(u, v, distance, parent)

    # weryfikacja
    for u in range(len(G)):   # sprawdzanie czy w grafie nie występuje ujemny cykl, przeglądamy jeszcze raz krawędzie
        for v in range(len(G)): # i jesli natrafimy na krawedz której koszt dojscia jest wiekszy to mamy cykl ujemny
            if G[u][v] != 0 and distance[v] > distance[u] + G[u][v]:
                return False

    return distance, parent

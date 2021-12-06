'''
Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
stwierdza czy dany graf zawiera dobry początek.
'''

'''
wykonujemy pierwszy raz algortym DFS i zapisujemy ostatni przetworzony wierzchołek, który może byc dobrym początkiem.
nastepnie wykonujemy drugi raz algorytm DFS z nową tablicą visited i zaczynajac od wierzchołka zapisanego. 
Sprawdzamy w tablicy visited czy wsyztskiego wierzchołki pozostałe były odiwedzone, jesli tak to znaczy, że
wierzchołek jest dobrym początkiem.
'''


def DFS(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if visited[v] is False:
            DFS(G, v, visited)

def good_start(G):
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u] is False:
            DFS(G, u, visited)
            start = u
    visited = [False for _ in range(len(G))]
    DFS(G, start, visited)
    for i in visited:
        if i is False:
            return False
    return True



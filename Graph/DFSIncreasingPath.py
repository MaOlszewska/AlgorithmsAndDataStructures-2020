'''Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
wierzchołków x i y oblicza ścieżkę, która prowadzi z x do y po krawędziach o
malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).
'''

'''Wchodzimy tylko w te krawędzie które są mniejsze od poprzedniej i zapamiętujemy  wartość prev'''


def DFSVisit(G, s, t, prev, parent):
    if s == t:
        return True
    for edge in range(len(G)):
        if G[s][edge] != 0:
            if G[s][edge] < prev[s] :  # and G[s][edge] > prev[edge]
                prev[edge] = G[s][edge]
                parent[edge] = s
                if DFSVisit(G, edge, t, prev, parent):
                    return parent
            else:
                continue
    return False

def DFS_increasing_paths(G, s, t):
    n = len(G)
    prev= [0 for _ in range(n)]
    prev[s] = float('inf')
    parent = [None for _ in range(n)]
    parent = DFSVisit(G, s, t, prev, parent)

    curr = t
    path = []
    while curr != None:
        path.append(curr)
        curr = parent[curr]
    return path


G =[[0, 3, 5, 10, 0],
    [3, 0, 4, 6, 2],
    [5, 4, 0, 0, 0],
    [10, 6, 0, 0, 0],
    [0, 2, 0, 0, 0],]

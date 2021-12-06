'''
Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
graf reprezentowany jest przez macierz sasiedztwa A.
'''

'''
Wykonujemy algorytm DFS, w którym oznaczamy to, że chcemy dostać scieżki długości 3. Jesli taką scieżke znajdziemy to 
SPrawdzamy czy z wierzchołka w którym zakonczyliśmy mamy krawędz która łączy te wierzchołek i wierzchołekm w którym 
zaczęlismy. Jeśli jest to możliwe to oznacza, że w grafie istnieje cykl długości 4.
`to nie jest najelpsze rozwiązanie`
'''
def DFSvisit(G, u, start, n, visited):
    if n == 0:
        visited[u] = False
        if u in G[start]:
            return True
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            if DFSvisit(G, v, start, n - 1, visited):
                return True
    visited[u] = False
    return False


def cycle_4(G):
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if DFSvisit(G, u, u, 3, visited):
            return True
        visited[u] = True
    return False


G = [[1, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3]]
print(cycle_4(G))
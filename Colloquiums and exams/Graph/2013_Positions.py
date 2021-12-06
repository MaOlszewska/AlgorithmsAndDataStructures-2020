'''
Dana jest tablica A.
Gracz początkowo znajduje się na (zadanej) pozycji (x, y), dla której zachodzi A[y][x] == true.
Z danej pozycji wolno bezpośrednio przejść jedynie na pozycję, której dokładnie jedna
współrzędna różni się o 1, oraz której wartość w tablicy A wynosi true. Proszę napisać program
obliczający do ilu różnych pozycji może dojść gracz startując z zadanej pozycji (x, y).
'''

def create_graph(A):
    n = len(A)
    G = [[0 for _ in range(n * n)] for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            # prawo lewo
            if j + 1 < n and A[i][j] is True is A[i][j + 1]:
                G[i * n + j][i * n + j + 1] = 1
                G[i * n + j + 1][i * n + j] = 1
            # góra dół
            if i + 1 < n and A[i][j] is True is A[i + 1][j]:
                G[i * n + j][i * n + n + j] = 1
                G[i * n + n + j][i * n + j] = 1
    return G

def DFS_visit_matrix(G, u, visited):
    visited[u] = True
    for v in range(len(G)):
        if visited[v] == False and G[u][v] != 0:
            DFS_visit_matrix(G, v, visited)

def positions(A, x, y):
    G = create_graph(A)
    visited = [False for _ in range(len(A) * len(A))]
    visited[x * len(A) + y ] = True
    DFS_visit_matrix(G, x * len(A) + y, visited)
    count = 0
    for i in visited:
        if i:
            count += 1
    return count - 1

A = [[True, True, True, False],
     [True, False, True, True],
     [True,True, False, False],
     [False,True, False, True]]


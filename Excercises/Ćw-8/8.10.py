'''
Kapitan pewnego statku zastanawia
się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
(n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
(to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
rozwiązującą problem kapitana.
'''

'''
Tworzymy nowy graf, gdzie ilośc wierzchołków to będzie ilośc pól na mapie i bedą one połączone krawędziami
ale tylko te krawędzie będą tam, gdzie staetk może wpłynąć.
Następie uywamy algorytmu DFS żeby, sprawdzić czy statek może odbyć taką podróż.
'''
def create_graph(G, T):
    n = len(G)  # wiersz
    m = len(G[0])  # kolumny
    new_graph = []
    for i in range(n):
        for j in range(m):
            neigbours = []
            # prawo
            if i * m + 1 + j < m + m * i and G[i][j + 1] > T and G[i][j] > T:
                neigbours.append(i * m + 1 + j)
            #dół
            if i * m + j + m < n * m and G[i + 1][j] > T and G[i][j] > T:
                neigbours.append(i * m + j + m)
            # lewo
            if i * m - 1 + j >= m * i and G[i][j - 1] > T and G[i][j] > T:
                neigbours.append(i * m - 1 + j)
            # góra
            if i * m + j - m >= 0 and G[i - 1][j] > T and G[i][j] > T:
                neigbours.append(i * m + j - m)
            new_graph.append(neigbours)
    return new_graph


def DFS_visit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if visited[v] is False:
            if v == len(visited) - 1:
                return True
            if DFS_visit(G, v, visited):
                return True
    return False


def capitan(M, T):
    G = create_graph(M, T)

    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u] is False:
            if DFS_visit(G, u, visited):
                return True
    return False

M = [[10, 4, 6, 10],
     [11, 8, 4, 4],
     [8, 9, 10, 11]]
M1 = [
     [3, 1, 4, 5, 5],
     [4, 2, 3, 2, 5],
     [3, 1, 1, 1, 5],
     [3, 3, 3, 3, 3],
     [1, 1, 4, 2, 5]
     ]
print(capitan(M1, 2))

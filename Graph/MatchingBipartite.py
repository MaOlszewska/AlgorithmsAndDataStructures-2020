# algorytm znajdujący maksymalne skojarzenie w grafie dwudzielnym

'''
Mając 2 zbiory wyznaczone przez graf dwudzielny (A i B) możemy wyznaczyć maksymalne skojarzenie poprzez dodanie
super-źródła i super-ujścia i założenie, że każda krawędź ze zbioru A jest skierowana do zbioru B oraz jej
przepustowość wynosi 1. Maksymalnym skojarzeniem jest maksymalnym przepływ od super-źródła do super-ujścia.
'''


from queue import Queue
# ford-fulkerson
def BFS_matrix(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    parent = [None] * len(G)

    visited[s] = True


    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                parent[each] = u
                Q.put(each)

    return visited[t]

def Ford_Fulkerson(G, s, t):
    parent = [None] * len(G)
    flow = 0

    while BFS_matrix(G, s, t, parent):

        # szukamy krawędzi o najmniejszej pojemności rezydualnej (czyli
        # największego przepływu jaki może być na danej ścieżce)
        # idziemy od ujścia po parentach w górę
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parent[current]][current] < cur_flow:
                cur_flow = G[parent[current]][current]
            current = parent[current]

        # po przejściu ścieżki zwiększamy flow o najmniejszą pojemność
        # rezydualną na tej ścieżce (cur_flow)
        flow += cur_flow

        # aktualizujemy pojemności rezydualne istniejących krawędzi oraz
        # krawędzi powrotnych, znowu idziemy od ujścia po parentach w górę
        v = t

        while (v != s):
            G[parent[v]][v] -= cur_flow
            G[v][parent[v]] += cur_flow
            v = parent[v]
    # g.printG()
    return flow


def max_matching(G):
    # tworzymy nową macierz, gdzie super-źródło(S) ma indeks len(matrix)-2, a super-ujście(T) - len(matrix-1)

    matrix = [[0] * (len(G) + 2) for _ in range(len(G) + 2)]

    S = len(matrix) - 2
    T = len(matrix) - 1

    for i in range(len(G)):
        for j in range(len(G)):
            matrix[i][j] = G[i][j]

            # dodajemy krawędzi od super-źródła i do super-ujścia
            if G[i][j] == 1:
                matrix[S][i] = 1
                matrix[j][T] = 1

    return Ford_Fulkerson(matrix, S, T)
'''
Dany jest zbiór N zadań, gdzie niektóre zadania muszą być wykonane przed innymi zadaniami.
Wzajemne kolejności zadań opisuje dwuwymiarowa tablica T[N][N]. Jeżeli T[a][b] = 1 to wykonanie zadania a musi
poprzedzać wykonanie zadania b. W przypadku gdy T[a][b] = 2 zadanie b
musi być wykonane wcześniej, a gdy T[a][b] = 0 kolejność zadań a i b jest obojętna. Proszę zaimplementować funkcję
tasks(T), która dla danej tablicy T, zwraca tablicę z kolejnymi numerami zadań do wykonania.
'''

def topologicSort(G):
    def DFSvisit(G, u):
        visited[u] = True
        for each in range(len(G)):
            if visited[each] == False and G[u][each] == 1:
                parent[each] = u
                DFSvisit(G, each)
        tpSorted.insert(0,u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    tpSorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each )
    return tpSorted



def transformGraph(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i == j: T[i][j] = -1
            elif T[i][j] == 1: T[j][i] = -1
            elif T[i][j] == 2:
                T[i][j] = -1
                T[j][i] = 1
            elif T[i][j] == 0:
                T[i][j] = 1
                T[j][i] = -1
    return T


def task(T):
    T = transformGraph(T)
    T = topologicSort(T)
    return [i for i in range(len(T))]  # domyslny wynik [0,1,2,... ]

T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]
print(task(T))


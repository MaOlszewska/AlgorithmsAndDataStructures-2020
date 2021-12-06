'''
Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
{1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach
'''

'''
Jest to standardowy algorytm BFS z dopisanym warunkiem w którym sprawdzamy czy kolejna krawędz jest mniejsza 
od poprzedniej'''
from queue import Queue


def decreasing_path(G, x, y):
    n = len(G)
    Q = Queue()
    Q.put(x)
    parent = [ float('inf') for _ in range(n)]
    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if G[u][v] != 0:
                if G[u][v] < parent[u]:
                    parent[v] = G[u][v]
                    Q.put(v)
                    if v == y:
                        return True
    return False

G = [[0, 10,15,0],
     [10,0,11,20],
     [15,11,0,17],
     [0,20,17,0]]
print(decreasing_path(G,0,3))
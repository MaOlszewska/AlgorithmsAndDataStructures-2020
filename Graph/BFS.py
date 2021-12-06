from queue import Queue

def BFS(G):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    visited[0] = True
    Q.put(0)
    path = []
    while Q.qsize() != 0:
        v = Q.get()
        path.append(v)
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                Q.put(u)
    return path
graf = [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]

def BFSmatrix(G):
    n = len(G)
    visited = [ False for _ in range(n)]
    parents = [ -1 for _ in range(n)]
    distance = [ 0 for _ in range(n)]
    Q = Queue()
    Q.put(0)
    visited[0] = True
    while Q.qsize() != 0:
        v = Q.get()
        for u in range(n):
            if G[v][u] != 0 and visited[u] is not True:
                visited[u] = True
                parents[u] = v
                distance[u] = distance[v] + 1
                Q.put(u)
    return distance, parents


# klasa opisująca informacje o każdym z wierzchołków, potrzebna do pracy BFS'a
class Vertix:
    def __init__(self):
        self.distance = 0
        self.visited = False
        self.parent = None


# funkcja zwraca listę numerów wierzchołków, do których można dojść z wierzchołka nr s
def neighbours(G, s):
    neighbour = []
    for i in range(len(G[s])):
        if G[s][i] == 1:
            neighbour.append(i)
    return neighbour


def BFS(G, s):
    Q = []  # Kolejkaa
    vertices = []  # tablica z informacjami o każdym z wierzchołków

    for _ in range(len(G)):    # informacje o każdym wierzchołku  distance, visited, parent
        vertices.append(Vertix())

    vertices[s].visited = True  # ustawiam dla wierzchołka s prawdę bo z niego zaczynam czyli jest odwiedzony już
    Q.append(s)   # dodaje go do kolejki

    while Q:   # dopóki kolejka jest nie pusta
        u = Q.pop(0)   # pobieram do zmiennej u wierzchołek
        print(u)  # wypisuje po kolejki wierzchołki jakie są odwiedzane
        for v in neighbours(G, u):   # przehcodzę po wszystkich sąsiadach wierzchołka   u
            if not vertices[v].visited:  # jeśli nie były odwiedzone to je odwiedzam i ustalam wartości visited distance i parentsa
                vertices[v].visited = True
                vertices[v].distance = vertices[u].distance + 1
                vertices[v].parent = u
                Q.append(v)   # dodaje ten wierzchołek do kolejki, i  to on bedzie moim wyjściowym wierzchołkiem
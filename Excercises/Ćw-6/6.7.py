'''
Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
2. Zadanie jak wyżej, ale każdy odcinek ma koszt i pytamy o minimalny koszt uzyskania odcinka [a, b].
3. Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków.
'''


def DFS_visit(G, u, visited, b):
    visited[u] = True
    for v in range(len(G)):
        if G[u][v] != 0:
            if visited[v] is False:
                if v == b:
                    return True
                if DFS_visit(G, v, visited, b):
                    return True
    return False

def create_graph(intervals):
    intervals = sorted(intervals, key = lambda x: x[1])
    n = intervals[len(intervals) - 1][1]

    G = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in intervals:
        G[i[0]][i[1]] = G[i[1]][i[0]] = 1
    return G

def stick_interval(intervals, a ,b):
    G = create_graph(intervals)
    visited = [False for _ in range(len(G))]
    if DFS_visit(G, a, visited, b):
        return True
    return False

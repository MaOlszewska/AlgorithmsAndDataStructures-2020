'''
Proszę zaimplementować algorytm BFS tak, żeby znajdował
najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
do wskazanego wierzchołka.
'''

from queue import Queue


def BSF_shortest_path(G, s, t):
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    path = []
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] is False:
                visited[v] = True
                parent[v] = u
                Q.put(v)
                if v == t:
                    while v is not None:
                        path.append(v)
                        v = parent[v]
                    path.reverse()
                    return path


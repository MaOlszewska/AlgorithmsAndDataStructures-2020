'''
Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
'''

'''
Sortujemy topologicznie graf, pierwszy z lewej wierzchołek jest naszym wierzchołkiem S, nastepnie wykonujemy algorytm BFS
i zapisuejmy dystanse, każdego wierzhołka.
'''
from queue import Queue


def DFSvisit(G, u, parent, topologycklySorted, visited):
    visited[u] = True
    for each in G[u]:
        if not visited[each]:
            parent[each] = u
            DFSvisit(G, each, parent, topologycklySorted, visited)
    topologycklySorted.insert(0, u)

def topologycSort(G):

    visited = [False] * len(G)
    parent = [None] * len(G)
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each, parent, topologycklySorted, visited)
    return topologycklySorted


def BFS(G, s):
    Q = Queue()
    distance = [float('inf')] * len(G)
    parent = [-1] * len(G)
    visited = [False] * len(G)
    visited[s] = True
    distance[s] = 0
    Q.put(s)
    while Q.qsize() != 0:
        u = Q.get()
        for each in G[u]:
            if not visited[each]:
                visited[each] = True
                distance[each] = distance[u] + 1
                parent[each] = u
                Q.put(each)

    return distance


G = [[1, 2, 3],
     [2],
     [4],
     [4],
     [5],
     []]
graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]

def shortestPathsInDag(G):
    TPsorted = topologycSort(G)
    print((TPsorted))
    distance = BFS(G, TPsorted[0])
    return distance


print(shortestPathsInDag(graph))
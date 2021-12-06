'''Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
innych w acyklicznym grafie skierowanym?'''

from queue import Queue


def topologycSort(G):
    def DFSvisit(G, u):
        nonlocal time
        time += 1
        # u.entry_time = time
        visited[u] = True

        for each in G[u]:
            if not visited[each]:
                parent[each] = u
                DFSvisit(G, each)
        time += 1
        # u.process_time = time
        topologycklySorted.insert(0, u)

    visited = [False] * len(G)
    parent = [None] * len(G)
    time = 0
    topologycklySorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each)

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


def shortestPathsInDag(G):
    TPsorted = topologycSort(G)
    print(TPsorted)
    distance = BFS(G, TPsorted[0])
    return distance


print(shortestPathsInDag(G))
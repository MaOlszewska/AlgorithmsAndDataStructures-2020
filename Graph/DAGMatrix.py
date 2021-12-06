'''Ułożenie wierzchołków w takiej kolejności, że krawędzie wskauzją tylko z lewej na prawą, w skierowanycm grafie acyklicznym'''

def DFSvisit(G, u, visited, parent, tpSorted):
    visited[u] = True
    for each in range(len(G)):
        if visited[each] == False and G[u][each] != 0:
            parent[each] = u
            DFSvisit(G, each)
    tpSorted.insert(0, u)


def topologicSort(G):
    visited = [False] * len(G)
    parent = [None] * len(G)
    tpSorted = []
    for each in range(len(G)):
        if not visited[each]:
            DFSvisit(G, each, visited, parent, tpSorted)
    return tpSorted

'''
Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem
NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznymgrafie skierowanym.
'''

def dfs_rec(graph,start,path, visited):
    visited[start] = True
    for edge in graph[start]:
        if edge not in path:
            #print(edge, path)
            dfs_rec(graph, edge,path, visited)
    path.insert(0,start)

def TopologicSort(G):
    path = []
    visited = [False for _ in range(len(G))]
    for u in range(len(G)):
        if visited[u] == False:
            dfs_rec(G, u, path, visited)
    return path


def HamiltonPathDAG(G):
    TPsort = TopologicSort(G) # posortowanie wierzchołków, które będą w koljeności rosnacej
    curr = 0
    while curr < len(G) - 1:  # ścieżka istnieje wtedy kiedy możemy po kolei przjesc przez kazdy wierzchołek nie pomijajac ani jednog i nie wracajac do poprzednich
        if (curr + 1 ) in TPsort:
            curr += 1
        else:
            return False
    return True

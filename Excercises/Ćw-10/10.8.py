'''
Dany jest acykliczny, spójny, nieskierowany, ważony graf T (czyli T jest
tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego
odległość do najdalszego wierzchołka jest minimalna.
'''


'''
Wykonuje dla każdego wierzchołka algorytm BFS i zwracam najwiekszy dystans pomiedzy tym wierzchołkiem i jakimś innym.
Póżniej wybieram tą odległosc ktora jest najmniejsza.
'''


from queue import Queue


def BFS(G, s):
    visited = [False for _ in range(len(G))]
    distance = [ 0 for _ in range(len(G))]
    Q = Queue()
    visited[s] = True
    Q.put(s)
    distance[s] = 0
    while Q.qsize() != 0:
        v = Q.get()
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                distance[u] = distance[v] + 1
                Q.put(u)
    return max(distance)

def bestroot(G):
    best = float('inf')
    bestroot = -1
    for i in range(len(G)):
        curr = BFS(G, i)
        if curr < best:
            best = curr
            bestroot = i
    return bestroot

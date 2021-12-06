'''Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza.
 Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń.'''

''
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

if __name__ == '__main__':
    G = [[2],
         [2],
         [0, 1, 3],
         [2, 4],
         [3, 5, 6],
         [4],
         [4]]
    print(bestroot(G))

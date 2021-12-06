'''
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa
może być dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która
przyjmuje nieskierowany, spójny i acyckliczny graf G (reprezentowany w postaci listy sąsiedztwa) i
wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym wierzchołku drzewa była możliwie najmniejsza.
Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić dowolny z
nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0.
'''


''' N razy bfs i szukamy minimum z wyników'''
from queue import Queue

def BFS(G, i):
    visited = [False for _ in range(len(G))]
    Q = Queue()
    visited[i] = True
    Q.put(i)
    distance = [0 for _ in range(len(G))]
    while Q.qsize() != 0:
        v = Q.get()
        for u in G[v]:
            if visited[u] == False:
                visited[u] = True
                Q.put(u)
                distance[u] = distance[v] + 1
    return max(distance)


def best_root(L):
    n = len(L)
    minimum = float('inf')
    idx = None
    for i in range(n):
        curr = BFS(L, i)
        if curr < minimum:
            minimum = curr
            idx = i
    return idx

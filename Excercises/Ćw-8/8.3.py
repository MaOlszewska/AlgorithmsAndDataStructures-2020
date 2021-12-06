'''
Proszę zaimplementować następujące algorytmy:
1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).
2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania
'''

from queue import Queue

# 1
'''
Żeby sprawdzić czy graf jest dwudzielny używamy do tego DFS lub BFS (tutaj BFS).
Tworzymy tablice z kolorami. Żeby graf był dwudzielny nie może isnieć krawędz między wierzchołakmi w tym samym kolorze.
Więc dla pierwszego wierzchołka ustawiamy kolor pierwszy, dla wszystkich wierzchołków, które są połaczone krawędzią
z tym wierzchołkiem ustawiamy kolor przeciwny. Sprawdzamy czy kolor poprzednika nie jest taki sam jak aktualnie 
przetwarzanego wierzchołka, jeśli tak to znaczy ze graf nie jest dwudzielny. 
Przy implementacji możemy użyć tablicy w której bedziemy mieć wartości True i False, które będą oznaczać dwa kolory.
Ułatwia to implenetacje przy zmianie koloru.
'''
def bipartite(G):
    Q = Queue()
    color = [None for _ in range(len(G))]
    color[0] = True
    Q.put(0)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v != u:
                if color[v] is None:
                    Q.put(v)
                    color[v] = not color[u]
                elif color[u] is color[v]:
                    return False
    return True

# 2
'''
Żeby oliczyć liczbę spójnych składowych grafu wystarczy, że użyjemy algorytmu DFS i bedziemy zwiększać licznik
skłądowych za każdym razem kiedy będziemy zaczynać od nowego nie przetworzonego wcześniej wierzchołka.
Takie coś oznacza, że graf składa się z rozłącznych podgrafów.
'''

def DFSvisit(G, u, visited):
    visited[u] = True
    for v in G[u]:
        if visited[v] is False:
            DFSvisit(G, v, visited)


def connected_component(G):
    visited = [False for _ in range(len(G))]
    count = 0
    for u in range(len(G)):
        if visited[u] is False:
            count += 1
            DFSvisit(G, u, visited)

    return count

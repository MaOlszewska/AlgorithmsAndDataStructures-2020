from queue import Queue


def bipartite_graph(G): # sprawdzam czy graf jest dwudzielny
    Q = Queue()  # tworzę kolejkę
    color = [None for _ in range(len(G))] # tworzę tablice z kolorami i na początku każdemu wierzchołkowi ustawiam kolor na None, bo nie wiadomo jaki bedzie
    color[0] = True  # dla wierzchołka o numerze  0 ustawiam kolor na true
    Q.put(0)  #dodaje do kolejki ten wierzchołek - 0

    while Q :   # dopóki kolejka nie jest pusta
        s = Q.get()  # biorę pierwszy element kolejki
        for v in G[s]:  #przechodzę po każdym sąseidzie wierzchołka s
            if v != s: #sprawdzam czy te wierzchołki nie są takie same
                if color[v] == None:  #jesli kolor wierzchołka v jest None to dodaje go do koeljki bo bedzie nastepnym do sprawdzenia
                    Q.put(v)     # i usatwiam jego kolor na przeciwny do koloru wierzchołka poprzendiego s
                    color[v] = not color[s]
                elif color[v] == color[s]:   # jesli kolory dwóch sąsiednich wierzchołków są takie same to zwracam False, bo to onznacza ze graf nie jest dwudzielny
                    return False
    return True
G = [[3, 5, 6], [5, 6], [4], [4, 0], [3, 2, 6], [1, 0], [1, 0, 4]]
bipartite_graph(G)

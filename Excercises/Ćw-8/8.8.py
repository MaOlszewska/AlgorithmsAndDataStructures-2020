'''
Dany jest graf G = (V, E), którego wierzchołki reprezentują punkty
nawigacyjne nad Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy
korytarz powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem jeśli pułap samolotu różni się od optymalnego najwyżej o t
metrów. Proszę zaproponować algorytm (bez implementacji), który sprawdza czy istnieje możliwość przelotu
z zadanego punktu x ∈ V do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie zmieniał pułapu.
Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować jego złożoność czasową
'''

'''
Algorytm BFS i modyfikacją taką, że dodajemy warunek kótry będzie sprawdzać czy samolot mieści się w granicach 
optymalnego pułapu. Moduł z róźnicy wysokosci aktualnego wierzchołka i liczby t musi być mniejszy od liczby p.
'''

from queue import Queue

def plane(G, x, y, t, p):
    Q = Queue()
    visited = [False for _ in range(len(G))]
    visited[x] = True
    Q.put(x)
    while not Q.empty():
        u = Q.get()
        for v in range(len(G)):
            if G[u][v] != 0 and abs(G[u][v] - t) <= p and visited[v] is False:
                Q.put(v)
                if v == y:
                    return True
        visited[u] = True
    return False

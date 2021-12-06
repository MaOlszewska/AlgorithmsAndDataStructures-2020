

def find_neighbours(G, v): # w tej funkcji wyznaczam sąsiadów każdego z wierzchołków i tworze z nich listę, którą póżniej wstawiam do kolejnej listy z
    neighbours = []        # sąsiadami wierzchołków na odpwoiednnie miejsca, które wyznacza numer wierzchołka
    for i in range(len(G[v])): # przechodzą po kolejnych elementach macierzy w wierszu o numerze v i kiedy natrafię na cyfrę 1 to znaczy że istenieje wierzchołek miedzy którym
        if G[v][i] == 1:       # jest krawędz -> wpisuje numer kolumny do listy sąsiadów wierzchołka v
            neighbours.append(i)
    return neighbours

def DFS(u, G, deleted, neighbour, cycle, vertex_counter):  # zmodyfikowana funkcja DFS, nie zgubi żadnego z cyklu składającego się na cykl eulera, bo zawsze bedzie ona wracać do wierzchołka w którym są jescze inne krawędzie do przejścia
    for v in neighbour[u]: # przechodzę po sąsiadach wierzchołka wyjściowego
        if deleted[u][v] == False: # jesli krawędz miedzy nimi nie została jescze ujęta w cykl to  zamieniam wartości w tablicy z usunietymi krawędziami
            deleted[u][v] = True
            deleted[v][u] = True
            cycle = DFS(v, G, deleted, neighbour, cycle, vertex_counter) # wywołuje koljny raz DFS tym razem z wierzchołkiem wyjściowym który jest sąsiadem poprzedniego
            cycle.append(u)  # doklejam wierzchołek do tablicy wynikowej po przetworzeniu
            if not u in vertex_counter: # sprawdzam czy wierzchołek był już użyty, jesli nie to wstawaim go do listy
                vertex_counter.append(u)
    return cycle

def euler( G ):
    neighbours = []
    for i in range(len(G)):       # tworzę liste z sąsiadami każdego wierzchołka, i przy oakzji sprawdzam czy każdy z wierzchółków ma parzystą liczbę sąsiadów
        n = find_neighbours(G, i) # nierówną zero, jesli liczba ta jest nieparzysta można odrazu stwierdzic, że cykl Eulera nie istnieje
        if len(n) == 0 or len(n) % 2 != 0:
            return None
        neighbours.append(n)

    deleted = [[False for _ in range(len(G))] for _ in range(len(G))]  # tworzę macierz, w której bedą zaznaczane krawędzie które zostały już użyte w szukaniu cyklu
    c = [0] # lista w której będą zapisane odpowiednie wierzchołki cyklu
    vertex_counter = []  # lista gdzie będą zaznaczane wierzchołki  już użyte, pomocna przy stwierdzeniu czy graf jest spójny czy nie
    cycle = DFS(0, G, deleted, neighbours, c, vertex_counter)
    if len(vertex_counter) != len(G): # jeśli liczba wierzchołków użytych w znalezionym cyklu jest różna od liczby wszytskich wierzchołków grafu to zanczy ze jest on niespójny
        return None
    return cycle

G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

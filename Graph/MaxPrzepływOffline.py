#Algorytm wykorzystuje utworzenie maksymalnego drzewa rozpinającego
#za pomocą algorytmu Prima. Następnie mając utworzone maksymalne
#drzewo rozpinające przechodzą po tablicy parentów zwróconej przez
#algorytm prima znajdujemy ścieżkę między szukanymi punktami.
#W naszym algorytmie krawędź o najmniejszej wadze na naszej scieżce
#miedzy szukanymi punktami będzie maksymalna przepustowoscia naszej ścieżki
#Złożoność O(E * logV)

from queue import PriorityQueue

def prim(G, v): #standartowy algorytm prima z wykładu ze zmianą w kolejce priorytetowej
    Q = PriorityQueue() #symulującą kolejkę priorytetowa typu max za pomoca wartosci ujemnych
    W = [float('-inf')] * len(G)
    Q.put((0, v))
    W[v] = 0
    parent = [None] * len(G)
    processed = [False] * len(G) #tablica przetworzonych wierzchołków

    while Q.qsize():
        _ , t = Q.get()
        for u, w in G[t]:
            if not processed[u] and w > W[u]:
                W[u] = w
                parent[u] = t
                Q.put((((-1) * W[u], u)))
        processed[t] = True
    return(parent)

def max_extending_path( G, s, t ):
  P = prim(G, s)
  path = []
  curr = t
  while curr != None: #odtwarzamy ścieżkę
    path.append(curr)
    curr = P[curr]

  for i in range(len(path)//2): #odwracamy ścieżke aby spełniała warunki zadania
    path[i], path[len(path) - 1 - i] = path[len(path) - 1 - i], path[i]
  return path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,10), (2,11), (3,5)],
[(2,5)],
[(3,7), (5,3), (4,6)],
[(4,7), (5,4)],
[(5,5)],
[]]

print(max_extending_path(G,0 ,5))
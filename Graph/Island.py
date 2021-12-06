'''
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
'''

# Przechowujemy w każdym z wierzchołków trzy pola ( tutaj w postaci tablic ), które będą przechowywać informacje o
# każdy rodzaju środku transportu. W tablicy parent przehcowuje dla każdego wierzchołka rodzica jego także
# z odpowiedniego śrdoka transportu. Przechodizmy algorytmem dijkstry i zanim dokonamy relaksacji sprawdzamy czy
# czy aktualna krawedz nie jest tej samej klasy co ta z której do niej przyszliśmy. Relaksujemy krawedź sprawdzając
# każdy z dostępnym srdoków transportu. Wynikiem jest minium z cześci talbicy odpowiadające miastu docelowemu.


from queue import PriorityQueue
from math import inf

def islands(G, s, t):
    n = len(G)
    Q = PriorityQueue()
    D = [[inf, inf, inf] for _ in range(n)]
    D[s] = [0, 0, 0]
    Parent = [[(None, None)] * 3 for _ in range(n)]  # wierzchołek i rodzaj transportu
    Parent[s] = [(None, 1), (None, 5), (None,8)]
    Q.put((0, s))
    while not Q.empty():
        _, u = Q.get()
        for v in range(n):
            if G[u][v] > 0:
                for i in range(3):
                    if Parent[u][i][1] is not None and G[u][v] != Parent[u][i][1]:# sprawdzamy czy obecna krawedz nie jest takiej klasy jak poprzednia
                        curr = G[u][v]
                        if curr == 1:  # przeindeksowujemy aktualny środek transportu
                            curr = 0
                        elif curr == 5:
                            curr = 1
                        else:
                            curr = 2
                        options = [1, 5, 8]
                        for i in range(3):
                            if G[u][v] != options[i]:
                                if D[v][curr] > D[u][i] + G[u][v]: # standardowa relaksacja
                                    D[v][curr] = D[u][i] + G[u][v]
                                    Q.put((D[v][curr], v))
                                    Parent[v][curr] = (u, options[i])
    return min(D[t])


if __name__ == '__main__':
    G = [[0, 5, 1, 8, 0, 0, 0],
         [5, 0, 0, 1, 0, 8, 0],
         [1, 0, 0, 8, 0, 0, 8],
         [8, 1, 8, 0, 5, 0, 1],
         [0, 0, 0, 5, 0, 1, 0],
         [0, 8, 0, 0, 1, 0, 5],
         [0, 0, 8, 1, 0, 5, 0]]
    print(islands(G, 5, 2))  # 13
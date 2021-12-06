'''
Mamy dany graf skierowany G = (V, E) oraz funkcję c∶ E → N opisującą
przepustowość każdej krawędzi (liczbę jednostek towaru na godzinę, które mogą się przemieszczać krawędzią).
Poza tym mamy dany zbiór wierzchołków-fabryk S = {s1, . . . , sn} oraz zbiór wierzchołków-sklepów
T = {t1, . . . , tm}. Dla każdej fabryki si znamy liczbę pi określającą ile jednostek towaru na godzinę fabryka
może maksymalnie produkować. Jednocześnie dla każdego sklepu tj mamy liczbę qj , która mówi ile jednostek towaru
na godzinę musi do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się
zapewnić, żeby do każdego sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga jednocześnie
nie zmuszając żadnej fabryki do przekroczenia swoich możliwości produkcyjnych i nie przekraczając
przepustowości żadnej z krawędzi.
'''
'''
Tworzymy super-źródło oraz super-ujście, gdzie przepustowościami są odpowiednio max ilość towaru, jaką może wyprodukowac fabryka
oraz ilość towaru, jakiej wymagają poszczególne sklepy. Następnie wykorzystujemy algorytm do znalezienia max przepływu w tym grafie
i sprawdzamy, czy każda krawędź ze sklepu do ujścia jest maksymalnie obciążona - tj. czy da się dostarczyć całe zapotrzebowanie.
'''

from queue import Queue


# ford-fulkerson
def BFS_matrix(G, s, t, parent):
    Q = Queue()
    visited = [False] * len(G)
    parent = [None] * len(G)

    visited[s] = True


    Q.put(s)

    while Q.qsize() != 0:
        u = Q.get()
        for each in range(len(G)):
            if G[u][each] != 0 and not visited[each]:
                visited[each] = True
                parent[each] = u
                Q.put(each)

    return visited[t]

def Ford_Fulkerson(G, s, t):
    parent = [None] * len(G)
    flow = 0

    while BFS_matrix(G, s, t, parent):

        # szukamy krawędzi o najmniejszej pojemności rezydualnej (czyli
        # największego przepływu jaki może być na danej ścieżce)
        # idziemy od ujścia po parentach w górę
        current = t
        cur_flow = float("inf")

        while (current != s):
            if G[parent[current]][current] < cur_flow:
                cur_flow = G[parent[current]][current]
            current = parent[current]

        # po przejściu ścieżki zwiększamy flow o najmniejszą pojemność
        # rezydualną na tej ścieżce (cur_flow)
        flow += cur_flow

        # aktualizujemy pojemności rezydualne istniejących krawędzi oraz
        # krawędzi powrotnych, znowu idziemy od ujścia po parentach w górę
        v = t

        while (v != s):
            G[parent[v]][v] -= cur_flow
            G[v][parent[v]] += cur_flow
            v = parent[v]

    return flow

def check(G, factories, stores):
    matrix = [[0] * (len(G) + 2) for _ in range(len(G) + 2)]
    for i in range(len(G)):
        for j in range(len(G)):
            matrix[i][j] = G[i][j]

    f = len(matrix) - 2
    s = len(matrix) - 1

    # dodajemy krawędzi z super-źródła do fabryk
    for factory, weight in factories:
        matrix[f][factory] = weight

    # dodajemy krawędzi ze sklepów do super-ujścia
    for store, weight in stores:
        matrix[store][s] = weight

    for i in matrix:
        print(i)

    flow = Ford_Fulkerson(matrix, f, s)
    print(flow)

    # sprawdzamy czy każda krawędź z fabryki do super-ujścia została pokryta maksymalnie dane przez flow,
    # czyli czy suma wag krawędzi  == flow

    Sum = 0
    for i in range(len(stores)):
        Sum += stores[i][1]

    return Sum == flow
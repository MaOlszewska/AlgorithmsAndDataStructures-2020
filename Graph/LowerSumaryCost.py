'''Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.'''


# Tworzymy graf, w którym istnieją krawędzię pomiedzy tymi liczbami które, mają wspólną cyfre conajmniej jedną.
# Wagą każdej kraedzi jest moduł z różnicy liczb. Sortujemy rosnąco te liczby. Wykonujemy Dijkstre na tak zmodyfikownaym grafie.
# Wynikiem jest najkrótsza ścieżka pomiędzy liczbą pierwszą i ostatnią, jeśli nie da się dotrzeć to zwracamy -1.

from queue import PriorityQueue
from math import inf


def give_digits(num):
    nums = []
    while num > 0:
        nums.append(num % 10)
        num //= 10
    return nums


def digits_of_T(T):
    nums = [[] for _ in range(len(T))]
    for i in range(len(T)):
        nums[i] = give_digits(T[i])
    return nums


def create_graph(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]
    nums = digits_of_T(T)
    # print(nums)
    for liczba1 in range(n):
        for liczba2 in range(n):
            if liczba1 != liczba2:
                for cyfra in nums[liczba1]:
                    if cyfra in nums[liczba2]:
                        G[liczba1][liczba2] = abs(T[liczba1] - T[liczba2])
                        G[liczba2][liczba1] = abs(T[liczba1] - T[liczba2])
                        break
    return G


T = [123, 891, 688, 889, 257, 246]


def dijkstryMatrix(G, s):
    def relax(u, v):
        nonlocal Q
        if D[v] > D[u] + G[u][v]:
            D[v] = D[u] + G[u][v]
            Q.put((D[v], v))
            Parent[v] = u

    n = len(G)
    Q = PriorityQueue()
    D = [inf] * n
    Parent = [-1] * n
    processed = [False] * n  # tablica przetworzonych wierzchołków
    D[s] = 0
    Q.put((D[s], s))
    while not Q.empty():
        _, u = Q.get()
        if not processed[u]:
            for v in range(n):
                if G[u][v] > 0 and not processed[v]:
                    relax(u, v)
            processed[u] = True

    return D, Parent


def lowestSumaricCost(T):
    T = sorted(T)
    G = create_graph(T)
    distance, parents = dijkstryMatrix(G, 0)
    print(distance[len(G) - 1])


lowestSumaricCost(T)
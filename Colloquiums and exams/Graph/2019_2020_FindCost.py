'''
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.
'''

from queue import PriorityQueue
from math import inf

def if_number(num1, idx2, numbers):
    while num1 > 0:
        if num1 % 10 in numbers[idx2]:
            return True
        num1 //= 10
    return False


def create_graph(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]
    numbers = []
    for number in T:
        num = []
        while number > 0:
            num.append(number % 10)
            number //= 10
        numbers.append(num)

    for i in range(n):
        for j in range(n):
            if i != j:
                if if_number(T[i], j, numbers):
                    G[i][j] = G[j][i] = abs(T[i] - T[j])
    return G

def dijkstra(G, s,t):
    n = len(G)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0

    for i in range(n):
        pq.put((distance[i],i))

    while not pq.empty():
        _, v = pq.get()
        if not visited[v]:
            for u in range(n):
                if G[v][u] != 0:
                    if distance[v] + G[v][u] < distance[u]:
                        distance[u] = distance[v] + G[v][u]
                        pq.put((distance[u],u))
                        parent[u] = v
            visited[v] = True
    return distance[t]



def find_cost(P):
    P = sorted(P)
    G = create_graph(P)
    dist = dijkstra(G, 0, len(G) - 1)
    if dist is inf:
        return -1
    else:
        return dist
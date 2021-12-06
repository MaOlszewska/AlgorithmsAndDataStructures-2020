''' (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
wychodząca z t.
1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n^2))
2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.'''
def universal_vent(G):
    n = len(G)
    arr = [1] * n
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                arr[i] = 0
            elif i != j:
                arr[j] = 0
    for x in range(len(arr)):
        if arr[x] == 1:
            return x
    return False
G=[[0, 0, 0, 0, 1],
   [0, 0, 0, 0, 1],
   [0, 0, 0, 0, 1],
   [0, 0, 0, 0, 1],
   [0, 0, 0, 0, 0],]

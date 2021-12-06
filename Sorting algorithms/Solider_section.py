'''Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''

def partition(tab, p, r):  # O(n)
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i +=1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def select (A, l, r, k):
    if l == r:
        return
    q = partition(A, l, r)
    if q == k:
        return
    elif k < q:
        return select(A, l, q - 1, k)
    else:
        return select(A, q + 1, r, k)

def section(T, p, q):
    select(T, 0, len(T) - 1, p)
    select(T, p, len(T) - 1, q)
    return T[p: q + 1]

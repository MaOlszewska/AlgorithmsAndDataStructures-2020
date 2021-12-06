'''
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''

def partition(T, left, right):
    pivot = T[right]
    j = left
    for i in range(left, right + 1):
        if T[i] <= pivot:
            T[i], T[j] = T[j], T[i]
            j += 1
    return j - 1

def quick_select(T, left, right, k):
    if left == right:
        return T[left]
    mid = partition(T, left, right)
    if mid == k:
        return T[mid]
    elif k < mid:
        quick_select(T, left, mid - 1, k)
    else:
        quick_select(T, mid + 1, right, k)

def section(T, p, q):
    quick_select(T, 0, len(T) - 1, p)
    quick_select(T, p + 1, len(T) - 1, q)
    return T[p :q + 1]



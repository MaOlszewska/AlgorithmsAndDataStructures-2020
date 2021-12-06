'''
Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby
zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
partition.
'''

def partition(T, left, right):
    pivot = T[right]
    i = left - 1
    for j in range(left, right):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[right] = T[right], T[i + 1]
    return i + 1

def quicksort(T, left, right):
    while left < right:
        q = partition(T, left, right)
        if q - left < right - q:
            quicksort(T, left, q - 1)
            left = q + 1
        else:
            quicksort(T, q + 1, right )
            right = q - 1
    return T
'''
Proszę zaimplementować jeden ze standardowych algorytmów sortowania tablicy działający w
czasie O(n2) (np. sortowanie bąbelkowe, sortowanie przez wstawianie, sortowanie przez wybieranie).
'''

# Bąbelkowe
def bubble_sort(T):
    for i in range(len(T) - 1):
        for j in range(len(T) - 1 - i):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T

# Przez wstawianie
def insert_sort(T):
    for i in range(1, len(T)):
        value = T[i]
        k = i - 1
        while k >= 0 and T[k] > value:
            T[k + 1] = T[k]
            k = k - 1
        T[k + 1] = value
    return T

# Przez wybieranie
def selection_sort(T):
    l = len(T)
    for i in range(l):
        min = i
        for k in range(i + 1, l):
            if T[k] < T[min]:
                min = k
            T[i], T[min] = T[min], T[i]
    return T
'''
Proszę zaimplementować funkcję partition z algorytmu QuickSort
według pomysłu Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą od piwota, a
większy na mniejszą.
'''

def hoare_partition(T, left, right):
    pivot = T[left]
    i = left - 1
    j = right + 1
    while True:
        j -= 1
        while T[j] > pivot:
            j -= 1
        i += 1
        while T[i] < pivot:
            i += 1
        if j > i:
            T[i], T[j] = T[j], T[i]
        else:
            return j


def hoare_quicksort(T, left, right):
    if len(T) == 1:
        return T
    if left < right:
        q = hoare_partition(T, left, right)
        hoare_quicksort(T, left, q)
        hoare_quicksort(T, q + 1, right)
    return T

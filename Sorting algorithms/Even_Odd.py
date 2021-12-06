'''
Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
'''

def quicksort(T, p, r):   # O(nlogn)
    if p < r:
        q = partition(T, p, r)
        quicksort(T, p, q - 1)
        quicksort(T, q + 1, r)
    return T


def partition(T, p, r):  # O(n)
    pivot = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]

    return i + 1

def sort(T):
    even = []  # parzyste
    odd = []  # nieparzyste

    for i in range(len(T)):
        if T[i] % 2 == 0:
            even.append(T[i])
        else:
            odd.append(T[i])

    even = quicksort(even, 0, len(even) - 1)
    j = k = 0
    for i in range(len(T)):
        if j >= len(even):
            T[i] = odd[k]
            k += 1
        elif k >= len(odd):
            T[i] = even[j]
            j += 1
        else:
            if even[j] < odd[k]:
                T[i] = even[j]
                j += 1
            elif even[j] > odd[k]:
                T[i] = odd[k]
                k += 1
    return T

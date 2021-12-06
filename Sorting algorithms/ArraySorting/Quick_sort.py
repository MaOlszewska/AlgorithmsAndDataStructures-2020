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


# def magic_5(tab, first, last, k):
#     j = first  # zmienna zliczająca ilość median które uzyskam
#     for i in range(first, last + 1, 5):  # pętla "dzieląca" tablice na mniejsze 5 elementowe
#         if i + 4 < last:
#             quick_sort(tab, i, i + 4)  # sortuje tablice wewnątrz przedziałów
#             tab[i + 2], tab[j] = tab[j], tab[i + 2]
#         else:  # Przypadek gdy jakiś przedział ma mniej niz 5 elementów
#             quick_sort(tab, i, last)
#             tab[(i + last) // 2], tab[j] = tab[j], tab[(i + last) // 2]  # Biorę środek podprzedziału i zapisuje go na poczatku aby zaoszczędzić miejsca
#         j += 1
#
#     if j - first + 1 > 5:
#         magic_5(tab, first, j - 1,
#                 k)  # jeżeli liczba podziałów jest większa niż 5 to rekurencyjne wywołują funkcje magic_5 dla median
#     else:
#         quick_sort(tab, first, j - 1)  # w innym przypadku sortuje liste
#     pivot = (first + j) // 2  # wybieram środek listy jako pivot
#     tab[last], tab[pivot] = tab[pivot], tab[last]  # zamieniam ostatni element z pivotem aby partition ustawił za pivot przez nas wybraną miediane median
#     q = partition(tab, first, last)
#
#     if k == q:  # Sytuacja w której znaleźliśmy miejsce elementu
#         return tab[q]
#     elif k < q:
#         return magic_5(tab, first, q - 1, k)  # Sytuacja w której element jest mniejszy od naszej mediany
#     else:
#         return magic_5(tab, q + 1, last, k)  # Sytuacja w której element jest większy od naszej mediany
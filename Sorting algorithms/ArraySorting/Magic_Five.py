from random import randint, shuffle, seed


def partition(tab, first, last):  # Partition w wersji Lomuto
    pivot = tab[last]
    j = first

    for i in range(first, last):
        if tab[i] < pivot:
            tab[i], tab[j] = tab[j], tab[i]
            j += 1

    tab[j], tab[last] = tab[last], tab[j]
    return j


def quick_sort(tab, first, last):  # Wybrałem Quick_sort jako algorytm sortujący przedziały
    while first < last:  # Pozbycie się rekurencji ogonowej
        pivot = partition(tab, first, last)
        if pivot - first < last - pivot:  # Wybieranie ciągle mniejszego ciągu do rekurencji aby ograniczyć złożonośc pamięciową
            quick_sort(tab, first, pivot - 1)
            first = pivot + 1
        else:
            quick_sort(tab, pivot + 1, last)
            last = pivot - 1
    return tab


def magic_5(tab, first, last, k):
    j = first  # zmienna zliczająca ilość median które uzyskam
    for i in range(first, last + 1, 5):  # pętla "dzieląca" tablice na mniejsze 5 elementowe
        if i + 4 < last:
            quick_sort(tab, i, i + 4)  # sortuje tablice wewnątrz przedziałów
            tab[i + 2], tab[j] = tab[j], tab[i + 2]
        else:  # Przypadek gdy jakiś przedział ma mniej niz 5 elementów
            quick_sort(tab, i, last)
            tab[(i + last) // 2], tab[j] = tab[j], tab[(i + last) // 2]  # Biorę środek podprzedziału i zapisuje go na poczatku aby zaoszczędzić miejsca
        j += 1

    if j - first + 1 > 5:
        magic_5(tab, first, j - 1,
                k)  # jeżeli liczba podziałów jest większa niż 5 to rekurencyjne wywołują funkcje magic_5 dla median
    else:
        quick_sort(tab, first, j - 1)  # w innym przypadku sortuje liste
    pivot = (first + j) // 2  # wybieram środek listy jako pivot
    tab[last], tab[pivot] = tab[pivot], tab[last]  # zamieniam ostatni element z pivotem aby partition ustawił za pivot przez nas wybraną miediane median
    q = partition(tab, first, last)

    if k == q:  # Sytuacja w której znaleźliśmy miejsce elementu
        return tab[q]
    elif k < q:
        return magic_5(tab, first, q - 1, k)  # Sytuacja w której element jest mniejszy od naszej mediany
    else:
        return magic_5(tab, q + 1, last, k)  # Sytuacja w której element jest większy od naszej mediany


def linearselect(A, k):
    return magic_5(A, 0, len(A) - 1, k)  # Wywołanie funkcji


seed(42)

n = 100
for i in range(n):
    A = list(range(n))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")


def iSort (A, left, right):  # insertion sort
    for i in range(left, right + 1):

        while A[i - 1] > A[i] and i > left:
            A[i], A[i - 1] = A[i - 1], A[i]
            i = i - 1


def partition (A, left, right):
    id = magicznePiatki(A, left, right)
    x = A[id]
    i = left - 1
    A[id], A[right] = A[right], A[id]  # trzeba zamienic żeby pivot był "klasycznie" na koncu

    for j in range(left, right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1




def magicznePiatki (A, l, r):  # l - left, r - right, indeksy fragmentu talibyc na którym wykonuje się funckja

    if r - l <= 5:
        iSort(A, l, r)
        # zwraca indeks na element który jest pivotem zamiast wartości bo i tak cały czas operuje na głownej tablicy
        return (l + r) // 2

    else:
        n = (r - l + 1) // 5  # ilość wszystkich całkowitych 5 w tablicy
        j = l
        for i in range(n):
            first = l + i * 5  # początek 'piątki'
            last = first + 4  # koniec 'piątki'

            iSort(A, first, last)  # sortuje wnętrze piątki
            A[j], A[(first + last) // 2] = A[(first + last) // 2], A[
                j]  # wstawia mediane na odpowiednie miejsce na poczatku tablicy
            j += 1

        if (r + 1 - l) % 5 != 0:  # jezeli została część która nie jest pełną 5
            iSort(A, n * 5 + l, r)  # sortuje pozostałą część
            A[j], A[(5 * n + r + l) // 2] = A[(5 * n + r + l) // 2], A[j]
            j += 1

        return magicznePiatki(A, l, j - 1)
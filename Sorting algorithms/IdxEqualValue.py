''' Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne.
Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.
Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?
'''


def equal(T):
    left = 0
    right = len(T) - 1

    while left <= right:
        mid = (left + right) // 2
        if T[mid] == mid:
            return True
        elif T[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return False


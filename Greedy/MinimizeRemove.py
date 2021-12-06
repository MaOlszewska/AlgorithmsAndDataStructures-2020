''' Mając tablicę T składającą się z n dodatnich liczb całkowitych i liczbe całkowitą K, której
    zadaniem jest zminimalizowanie różnicy między maksimum i minimum w danej tablicy
    po usunięciu dokładnie K elementów.
'''

''' Różnica zostanie zmiimalizowana przez usunięcie minimalnego lub maksymalnego elementu z tablic.
    należy posortować tablice rosnąćo, nastepnie przejść K razy i zmieniać maksimim lub minimum na zero.'''


def minimumRange(T, K):
    n = len(T)
    T.sort()

    left = 0
    right = n - 1

    for i in range(K):
        if T[right - 1] - T[left] < T[right] - T[left + 1]:
            right -= 1
        else:
            left += 1
    return T[right] - T[left]


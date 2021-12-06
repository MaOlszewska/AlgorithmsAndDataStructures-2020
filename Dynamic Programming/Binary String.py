'''
Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) string'ów
długości n bez jedynek obok siebie.
'''

'''Rozdizelimy problem na dwa przypadki, wtedy kiedy string konczy się na 0 (jako nastepną liczbę
możemy dołożyć  0 lub 1), ale konczy się na 1(wtedy możemy dołożyć tylko 0).
Stowrzymy dwie tablice, w których pod indeksem i znajduje się liczba prawidłowych stringów długosci i.
uzupłęniamty tablice od początku biorąć coraz dłuzsze stringi przez doklejenie zera lub jednynki na koniec.
Wynikiem jest suma elementów na indeksie n w obu tablicach'''


def count_binary(n):
    zero = [ 0 for _ in range(n + 1)]
    one = [0 for _ in range(n + 1)]

    zero[1] = one[1] = 1

    for i in range(2, n + 1):
        zero[i] += zero[i - 1] + one[i - 1]
        one[i] += zero[i - 1]
    suma = zero[n] + one[n]
    return suma

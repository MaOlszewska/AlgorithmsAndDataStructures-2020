'''
Dana jest posortowana tablica A[1...n] oraz liczba x.
Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.
'''

'''
Sprawdzamy czy liczba na pierwszym i dstatnim indeksie w tablicy po dodaniu tworzą liczbę x.
Jesli suma jest wieksza od liczby x to zmnijeszamy indeks po prawej stronie, jesli jest mniejsza to zwiekszamy
indeks z lewej. Jeżeli indeksy z prawej i lewej się zrównają to znaczy, że nie ma takich liczb, które się sumują do x.
'''
def searchsum(A, x):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] > x:
            j -= 1
        else:
            i += 1
    return False

'''
Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne,
a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej
liczby naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma
jej w tablicy, to należy zwrócić None.
'''

def search(T, x):
    right = 1
    while True:
        if T[right] == None or T[right] > x:
            break
        else:
            right *= 2
    left = 0
    while left <= right:
        mid = (left + right) // 2

        if T[mid] == None or T[mid] > x:
            right = mid - 1
        elif T[mid] == x:
            return mid
        else:
            left = mid + 1
    return None





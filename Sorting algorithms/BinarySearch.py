'''Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz liczbę x i sprawdza,
czy x występuje w A. Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.
'''

def binarysearch_recursive(T, s, e, x):
    if s > e:
        return None
    mid = (s + e) // 2
    if T[mid] == x:
        return mid
    if T[mid] < x:
        return binarysearch_recursive(T, mid + 1, e, x)
    else:
        return binarysearch_recursive(T, s, mid - 1, x)

def binarysearch_iterative(T, x):
    left = 0
    right = len(T) - 1
    while left <= right:
        mid = (left + right) // 2
        if T[mid] == x:
            return mid
        elif T[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return None
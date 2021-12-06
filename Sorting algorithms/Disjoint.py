'''
Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest
znacznie mniejsze od n. Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.
'''

''' CZy każdy elemnt z wikszego zbioru znajdue sie w mniejszym posortowanym zbiorze'''

def binarysearch(T, s, e, x):
    if s > e:
        return None
    mid = (s + e) // 2
    if T[mid] == x:
        return mid
    if T[mid] < x:
        return binarysearch(T, mid + 1, e, x)
    else:
        return binarysearch(T, s, mid - 1, x)


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


def disjoint(T1,T2):
    T1 = quicksort(T1, 0, len(T1) -1)
    for i in T2:
        if binarysearch(T1, 0, len(T2) - 1, i) is None:
            return False
    return True

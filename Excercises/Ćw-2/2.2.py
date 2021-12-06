'''
Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].
'''

def inversion(T, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += inversion(T, left, mid)
        count += inversion(T, mid + 1, right)
        count += merge(T, left, right, mid)
    return count

def merge(T, left, right, mid):
    i, j, k = left, mid + 1, left
    count = 0
    while i <= mid and j <= right:
        if T[i] <= T[j]:
            k += 1
            i += 1
        else:
            count += mid - i + 1
            k += 1
            j += 1

    return count


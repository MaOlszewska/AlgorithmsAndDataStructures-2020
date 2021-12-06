'''
Proszę zaimplementować algorytm znajdowania k-go co do wielkości elementu w tablicy
n elementowej w “spodziewanym” czasie O(n)
'''

# Select
def partition(T, left, right):
    pivot = T[right]
    i = left - 1
    for j in range(left, right):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[right] = T[right], T[i + 1]
    return i + 1


def select (A, l, r, k):
    if l == r:
        return
    q = partition(A, l, r)
    if q == k:
        return
    elif k < q:
        return select(A, l, q - 1, k)
    else:
        return select(A, q + 1, r, k)
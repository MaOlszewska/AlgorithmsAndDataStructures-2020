'''Kolokwium I 15/16 zadanie 1'''
def partition(T, p, r):
    pivot = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def select(T, p, r, x):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if x == q:
        return T[x]
    elif x < q:
        return select(T, p, q-1, x)
    else:
        return select(T, q+1, r, x)


def SumSort(A,  n):
    for i in range(n, n * n, n):
        select(A, i - n, n * n - 1, i)
    return A
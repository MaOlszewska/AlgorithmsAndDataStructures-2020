'''
Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać
własny stos).
'''

def partition( T, left, right):
    pivot = T[right]
    i = left - 1
    for j in range(left, right):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[right] = T[right], T[i + 1]
    return i + 1


def quicksort_without_recursion(T):
    S = []
    left = 0
    right = len(T) - 1
    S.append((left, right))
    while len(S) > 0:
        (left, right) = S.pop()
        if left < right:
            q = partition(T, left, right)
            if q - left > right - 1:
                S.append((left, q - 1))
                S.append((q + 1, right))
            else:
                S.append((q + 1, right))
                S.append((left, q - 1))
    return T



'''
Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B, gdzie ∣B∣ = log n.
Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.
'''
from math import log2


def counting_sort(A, k):
    C = [0] * k
    B = [0] * len(T)
    print(C, B)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(len(T) - 1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    for i in range(len(T)):
        A[i] = B[i]


def insertion_sort(T):
    for i in range(len(T)):
        key = T[i]
        j = i-1
        while j >= 0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j  + 1] = key
    return T


def sort(T):
    A = [0] * int(log2(len(T)))
    counting_sort(T, len(A))
    return T
T = [2,1,2,3,0,0,3,0,3,3,3,3,3,2,2,0]
print(sort(T))
'''
Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
przyjmuje na wejściu dwie n^2-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
elementów z A
'''

def partition(T, left, right):
    pivot = T[right]
    j = left
    for i in range(left, right + 1):
        if T[i] <= pivot:
            T[i], T[j] = T[j], T[i]
            j += 1
    return j - 1

def quick_select(T, left, right, k):
    if left == right:
        return T[left]
    mid = partition(T, left, right)
    if mid == k:
        return T[mid]
    elif k < mid:
        quick_select(T, left, mid - 1, k)
    else:
        quick_select(T, mid + 1, right, k)

def Sum_Sort(A, n):
    for i in range(n, n * n, n):
        quick_select(A, i - n, len(A) - 1,  n)
    return A

'''
Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.
'''

def heapify(T, n, i):   # O(nlogn)
    l = 2 * i + 1  # lewy
    r = 2 * i + 2  # prawy
    m = i

    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)
    return T

def buildheap(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        heapify(T, n, i)
    return T

def insert(heap, value):
    n = len(heap)
    i = n
    heap.append(value)
    j = (i - 1) // 2
    while i > 0 and heap[j] < value:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap

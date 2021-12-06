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

def heapsort(T):
    n = len(T)
    buildheap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
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

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2


def heapify_max(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] > T[m]:
        m = l
    if r < n and T[r] > T[m]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify_max(T, n, m)


def heapify_min(T, n, i):
    l = left(i)
    r = right(i)
    m = i
    if l < n and T[l] < T[m]:
        m = l
    if r < n and T[r] < T[m]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify_min(T, n, m)


def buildheap_max(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_max(T, n, i)


def buildheap_min(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify_min(T, n, i)


def heapsort_max(T):
    n = len(T)
    buildheap_max(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify_max(T, i, 0)


def heapsort_min(T):
    n = len(T)
    buildheap_min(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify_min(T, i, 0)


def insert_into_heap_max(T, val):
    T.append(val)
    i = len(T) - 1
    j = parent(i)
    while T[j] < T[i] and j >= 0:
        T[j], T[i] = T[i], T[j]
        i = j
        j = parent(i)

    return T


def pop_from_heap_max(T):
    val = T[0]
    n = len(T)
    T[0], T[n - 1] = T[n - 1], T[0]
    heapify(T, n - 1, 0)
    T.pop()
    return val

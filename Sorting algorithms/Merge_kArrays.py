'''
    Zaproponuj algorytm scalający k posortowanych
    tablic w jedną posortowaną tablicę. Łączna liczba
    elementów we wszystkich tablicach wynosi n.
'''

''' Tworzymy kopiec Minimum z pierwszym elementem każdej z k list, doodając do kopca wartość i numer tablicy.
poźniej bierzemy element minimalny z kopca i dodajemy do niego kolejny elemnt z tej talbicy z której wyciągneliśmy min.
naprawiamy kopiec. O(log(k))'''

def heapify(T, n, i):   # O(nlogn)
    l = 2 * i + 1  # lewy
    r = 2 * i + 2  # prawy
    m = i

    if l < n and T[l][0] < T[m][0]:
        m = l
    if r < n and T[r][0] < T[m][0]:
        m = r
    if m != i:
        T[i], T[m] = T[m], T[i]
        heapify(T, n, m)
    return T


def buildheap(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
        T = heapify(T, n, i)
    return T


def insert(heap, value, k):
    n = len(heap)
    i = n
    heap.append((value, k))
    j = (i - 1) // 2
    while i > 0 and heap[j][0] > value:
        heap[i], heap[j]= heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap

def get_min(heap):
    Min = heap.pop(0)
    heap = heapify(heap, len(heap), 1)
    return Min

def sort(lists, n):
    k = len(lists)
    heap = []
    merged = []
    for i in range(k):
        heap.append((lists[i][0],i))
    heap = buildheap(heap)

    while len(merged) != n:
        Min, idx = get_min(heap)
        merged.append(Min)
        if len(lists[idx]) != 0:
            lists[idx].pop(0)
            if len(lists[idx]) != 0:
                insert(heap, lists[idx][0], idx)
    return merged
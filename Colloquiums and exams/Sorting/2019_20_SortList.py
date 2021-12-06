'''
Dana jest struktura realizująca listę jednokierunkową:

class Node:
    def __init__( self, val ):
    self.next = None
    self.val = val

Proszę napisać funkcję, która mając na wejściu ciąg tak zrealizowanych posortowanych list scala je
w jedną posortowaną listę (składającą się z tych samych elementów).
'''


class Node:
  def __init__( self, val ):
    self.next = None
    self.val = val

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

def parent(i):
    return (i - 1) // 2

def buildheap(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        T = heapify(T, n, i)
    return T

def buildheap_min(T):
    n = len(T)
    for i in range(n // 2 - 1, -1, -1):
       T = heapify(T, n, i)
    return T

def insert(heap, value, k):
    n = len(heap)
    i = n
    heap.append((value, k))
    j = (i - 1) // 2
    while i >  0 and heap[j][0] >= value:
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


def get_min(heap):
    _min, head = heap.pop(0)
    heapify(heap, len(heap) - 1,0)
    return _min, head

def tasks(lists):
    n = len(lists)
    heap = []
    merged = Node(None)
    curr = merged
    for i in range(n):
        heap.append((lists[i].val, lists[i]))
    heap = buildheap(heap)

    while len(heap) != 0:
        _min, head = get_min(heap)
        curr.next = head
        curr = curr.next
        head = head.next
        if head != None:
            insert(heap, head.val, head)
    return merged.next
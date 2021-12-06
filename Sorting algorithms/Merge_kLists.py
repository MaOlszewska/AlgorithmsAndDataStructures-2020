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
        heap[i], heap[j] = heap[j], heap[i]
        i = j
        j = (i - 1) // 2
    return heap


def get_min(heap):
    _min, head = heap.pop(0)
    heapify(heap, len(heap),1)
    return _min, head



class Node:
  def __init__(self):
    self.next = None
    self.val = None


def tab2list(T):
  H = Node()
  C = H
  for i in range(len(T)):
    X = Node()
    X.val = T[i]
    C.next = X
    C = X
  return H.next


def printlist(L):
    while L is not None:
        print( L.val, "->", end=" ")
        L = L.next
    print("|")


def sortLists(lists):
    n = len(lists)
    heap = []
    merged = Node()
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
L1 = tab2list([1,5,7])
L2 = tab2list([4,9,12,14])
L3 = tab2list([2,3,6,8])
L4 = tab2list([0,10,11])

Lists = [L1,L2,L3,L4]
merged = sortLists(Lists)
printlist(merged)
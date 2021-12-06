'''
Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{next; value;}
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
'''

class Node:

    def __init__(self):
        self.value = None
        self.next = None


def insertion_sort(f):
    if f.next == None:
        return None
    sortedlist = f
    f = f.next
    sortedlist.next = None
    while f != None:
        curr = f
        f = f.next
        if curr.value < sortedlist.value:
            curr.next = sortedlist
            sortedlist = curr
        else:
            search = sortedlist
            while search.next != None and curr.value > search.next.value:
                search = search.next
            curr.next = search.next
            search.next = curr
    return sortedlist


def tab2list(T):
  H = Node()
  C = H
  for i in range(len(T)):
    X = Node()
    X.value = T[i]
    C.next = X
    C = X
  return H.next


def printlist(L):
    while L is not None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")


def Sort(head):
    n = 0
    cp_head = head
    while cp_head is not None:
        n += 1
        cp_head = cp_head.next
    section = n / 10

    buckets = [Node() for _ in range(n)]

    cp_head = head
    while cp_head is not None:
        index = int(cp_head.value / section)
        bucket = buckets[index]
        while bucket.next is not None:
            bucket = bucket.next
        bucket.next = cp_head
        cp_head = cp_head.next
        bucket = bucket.next
        bucket.next = None

    for i in range(len(buckets)):
        if buckets[i].next is not None:
            if buckets[i].next.next is None:
                buckets[i] = buckets[i].next
            else:
                buckets[i] = insertion_sort(buckets[i].next)

    head_sorted = buckets[0]
    cp = head_sorted

    for i in range(1, len(buckets)):
        if buckets[i].value is not None:
            while cp.next is not None:
                cp = cp.next
            cp.next = buckets[i]
            cp = cp.next
    return head_sorted

T = [5,1,6,6.6,8,4,3,2.2,7.8,9.1,2]

head = tab2list(T)
printlist(Sort(head))


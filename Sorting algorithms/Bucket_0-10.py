'''Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
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


def bucket_on_list(head):
    n = 0
    cp_head = head
    while cp_head is not None:
        n += 1
        cp_head = cp_head.next

    section = 10 / n
    buckets = [Node() for _ in range(n)]
    cp_head = head
    while cp_head:
        idx = int(cp_head.value / section)
        tmp = buckets[idx]
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = cp_head
        cp_head = cp_head.next
        tmp = tmp.next
        tmp.next = None

    for i in range(len(buckets)):
        if buckets[i].next is not None:
            if buckets[i].next.next == None:
                buckets[i] = buckets[i].next
            else:
                buckets[i] = insertion_sort(buckets[i].next)

    sortedlist = buckets[0]
    p = sortedlist
    for i in range(1, len(buckets)):
        if buckets[i].value is not None:
            while p.next != None:
                p = p.next
            p.next = buckets[i]
            p = p.next
    return sortedlist

t = [0,1,3,2, 5.3,6.5,5,1.22,3.44,4.51,4.12]
L = tab2list(t)
printlist(L)
N = bucket_on_list(L)
printlist(N)
class Node:

    def __init__(self):
        self.value = None
        self.next = None


def insertion_sort(f):
    if f == None:
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


def bucket_sort(L):
    n = 0
    tmp = L
    while tmp != None:
        tmp = tmp.next
        n += 1

    section = 10 / n
    tab = [Node() for _ in range(n)]  # tablica wiaderek
    p = L
    while p:
        idx = int(p.value / section)
        tmp = tab[idx]
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = Node()
        tmp.next.value = p.value
        p = p.next

    for i in range(len(tab)):
        if tab[i].next != None:
            tab[i] = insertion_sort(tab[i].next)

    first = tab[0]
    p = first
    for i in range(1, len(tab)):
        if tab[i].value != None:
            while p.next != None:
                p = p.next
            p.next = tab[i]
            p = p.next

    return first


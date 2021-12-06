class Node():
    def __init__(self, val ):
        self.val = val
        self.next = None

def add(lista, w):
    p = Node(w)
    p.next = lista
    return p

def tab2list(T):
  H = Node()
  C = H
  for i in range(len(T)):
    X = Node()
    X.value = T[i]
    C.next = X
    C = X
  return H.next

def printlist(f):
    while f is not None:
        print(f.val, end=" ")
        f = f.next
    print("  ")

def insertion_sort(f):
    if f == None:
        return None
    f1 = f
    f = f.next
    f1.next = None
    while f !=  None:
        curr = f
        f = f.next
        if curr.val < f1.val:
            curr.next = f1
            f1 = curr
        else:
            search = f1
            while  search.next != None and curr.val > search.next.val:
                search = search.next
            curr.next = search.next
            search.next = curr
    return f1

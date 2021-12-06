class Node:

    def __init__(self):
        self.value = None
        self.next = None


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


def TwoList_split(L):
    even = Node()  # parzyste
    odd = Node()   # nieparzyste
    Even = even
    Odd = odd

    while L is not None:
        if L.value % 2 == 0:
            even.next = L
            even = L
            odd.next = None
        else:
            odd.next = L
            odd = L
            even.next = None
        L = L.next
    return Even.next, Odd.next



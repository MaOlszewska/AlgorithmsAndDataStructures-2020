'''
Dana jest struktura Node opisująca listę jednokierunkową:
struct Node { Node * next; int value; };
Proszę zaimplementować funkcję Node* fixSortedList( Node* L ), która otrzymuje na
wejściu listę jednokierunkową bez wartowanika. Lista ta jest prawie posortowana w tym sensie, że
powstała z listy posortowanej przez zmianę jednego losowo wybranego elementu na losową
wartość. Funkcja powinna przepiąć elementy listy tak, by lista stała się posortowana i zwrócić
wskaźnik do głowy tej listy. Można założyć, że wszystkie liczby na liście są różne i że lista ma co
najmniej dwa elementy. Funkcja powinna działać w czasie liniowym względem długości listy
wejściowej.
'''

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


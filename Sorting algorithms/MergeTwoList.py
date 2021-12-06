'''
Scalanie dwóch posortowanych list jednokierunkowych do jednej
'''

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def TabToList(A):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")


def merge(L1, L2):
    if L1 is None and L2 is None:
        return None
    elif L1 is None and L2 is not None:
        return L2
    elif L1 is not None and L2 is None:
        return L1

    mergeList = Node()
    H = mergeList
    while L1 is not None and L2 is not None:
        print(L1.value)
        if L1.value <= L2.value:
            mergeList.next = L1
            L1 = L1.next
        else:
            mergeList.next = L2
            L2 = L2.next
        mergeList = mergeList.next
    if L1 is None:
        mergeList.next = L2
    if L2 is None:
        mergeList.next = L1

    return H.next




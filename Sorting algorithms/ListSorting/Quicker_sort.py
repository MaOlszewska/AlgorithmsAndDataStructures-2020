class Node:
    def __init__(self):
        self.val = None
        self.next = None

def printlist(f):
    while f is not None:
        print(f.val, "-->", end = " ")
        f = f.next
    print("|")

def QuickerSort(f):
    if f is None:
        return f
    smaller = Node()
    small = smaller
    equal = Node()
    eq = equal
    greater = Node()
    great = greater

    pivot = f.val
    while f is not None:
        if f.val < pivot:
            small.next = f
            small = small.next
            eq.next = None
            great.next = None
        elif f.val == pivot:
            eq.next = f
            eq= eq.next
            small.next = None
            great.next = None
        else:
            great.next = f
            great = great.next
            eq.next = None
            small.next = None
        f = f.next
    return merge(QuickerSort(smaller.next), equal.next, QuickerSort(greater.next))

def merge(smaller, equal, greater):
    tmp = smaller
    while smaller is not None and tmp.next is not None:
        tmp = tmp.next

    tmp2 = equal
    while equal is not None and tmp2.next is not None:
        tmp2 = tmp2.next

    if smaller is not None:
        tmp.next = equal
        tmp2.next = greater
        return smaller
    else:
        tmp2.next = greater
        return equal
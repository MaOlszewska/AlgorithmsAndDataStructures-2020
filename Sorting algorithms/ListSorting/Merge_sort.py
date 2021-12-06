class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def add(f, w):
    p = Node(w)
    p.next = f
    return p


def printlist(f):
    while f is not None:
        print(f.val,"->",end = " ")
        f = f.next
    print(" ")


def mergesort(a, b):  # na posortowanych listach
    if a is None:
        return b
    if b is None:
        return a
    if a.val <= b.val:
        result = a
        result.next = mergesort(a.next, b)
    else:
        result = b
        result.next = mergesort(a, b.next)
    return result


def merge(f1, f2):
    f3 = None
    while f1 != None and f2 != None:
        if f1.val <= f2.val:
            f3 = add(f3, f1.val)
            f1 = f1.next
        else:
            f3 = add(f3, f2.val)
            f2 = f2.next

    while f1 != None or f2 != None :

        if f1 ==None :
            f3 = add(f3, f2.val)
            f2 = f2.next
        else:
            f3 = add(f3, f1.val)
            f1 = f1.next
    return f3


def reverse(f):
    if f.next is None:
        return f
    else:
        q= f
        p = f.next
        f = p.next
        q.next = None
        while f is not None:
            p.next = q
            q = p
            p = f
            f = f.next
        p.next = q
    return p


def Merge_sort(list):
    list1, list2 = partittion(list)
    while list2.next is not None:
        list = merge(list1, list2)
        list1, list2 = partittion(list)

    return list1


def partittion(list):
    a = list1 = Node(-1, None)
    b = list2 = Node(-1, None)
    append_to_list1 = True
    p = list
    v = p.val
    p = p.next
    while p is not None:
        if p.val < v:
            append_to_list1 = not append_to_list1

        if append_to_list1:
            a.next = p
            a = a.next
        else:
            b.next = p
            b = b.next
    return list1, list2

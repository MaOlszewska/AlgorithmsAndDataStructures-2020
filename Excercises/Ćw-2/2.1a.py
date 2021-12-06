'''
Proszę zaimplementować:
1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
'''


class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def printlist(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print("  ")


def TabToList(T):
    head = Node(None)
    curr_head = head
    for i in range(len(T)):
        X = Node(None)
        X.val = T[i]
        curr_head.next = X
        curr_head = X
    return head.next

def merge_sorted_list(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1

    mergelist = Node(None)
    tmp = mergelist
    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            mergelist.next = head1
            head1 = head1.next
        else:
            mergelist.next = head2
            head2 = head2.next
        mergelist = mergelist.next
    if head1 is None:
        mergelist.next = head2
    else:
        mergelist.next = head1

    printlist(tmp.next)

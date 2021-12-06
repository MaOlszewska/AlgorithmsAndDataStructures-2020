'''
Proszę zaimplementować funkcję odwracającą listę jednokierunkową.
'''

class Node():
    def __init__(self, val ):
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

def reverse(head):
    if head is None:
        return None
    prev = None
    tmp = head.next
    while head is not None:
        head.next = prev
        prev = head
        head = tmp
        if tmp is not None:
            tmp = tmp.next
    printlist(prev)

T = [1,2,3,4,5,6]
L = TabToList(T)
printlist(L)
reverse(L)
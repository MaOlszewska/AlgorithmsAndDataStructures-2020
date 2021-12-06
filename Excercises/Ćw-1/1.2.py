'''
Proszę zaimplementować algorytm sortowania listy
jednokierunkowej. W szczególności należy:
1. Zdefiniować klasę w Pythonie realizującą listę jednokierunkową.
2. Zaimplementować wstawianie do posortowanej listy.
3. Zaimplementować usuwanie maksimum z listy.
4. Zaimplementować sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyższych funkcji
'''

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def add(head, value):
    p = Node(value)
    p.next = head
    return p

def TabToList(T):
    head = Node()
    curr_head = head
    for i in range(len(T)):
        X = Node()
        X.value = T[i]
        curr_head.next = X
        curr_head = X
    return head.next

def printlist(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print("  ")

def insertion_sort(head):
    if head == None:
        return None
    curr_head = head
    head = head.next
    curr_head.next = None
    while head !=  None:
        curr = head
        head = head.next
        if curr.val < curr_head.val:
            curr.next = curr_head
            curr_head = curr
        else:
            search = curr_head
            while  search.next != None and curr.val > search.next.val:
                search = search.next
            curr.next = search.next
            search.next = curr
    return curr_head
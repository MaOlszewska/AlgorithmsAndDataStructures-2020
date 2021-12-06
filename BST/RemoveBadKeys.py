''' Mająć BST i zakres wartosci kluczy, usunąć wsyztskie te klucze które nie
zawierają się w tym przedziale.'''

class BSTNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.right = None
        self.left = None

def insert(root, key, value):
    prev = None    # trzyammy wskaźnik na poprzednika
    while root is not None:   # przechodzimy do końca naszego drzewa
        if key > root.key:  # sprawdzamy czy klucz jest wiekszy od aktualnego jesli tak to idzimey w prawo, i zapisujemy poprzednika
            prev = root
            root = root.right
        else:
            prev = root   # jesli nie to idzimey w lewo i też zapisujemy poprzednika
            root = root.left

    if key < prev.key:   # jeśli wstawiany klucz jest mniejszy od poprzendika swojego to wstawiamy bo na lewo
        prev.left = BSTNode(key, value)
        prev.left.parent = prev

    else:  # jeśli większy to na prawo, a jego rodzica ustawiamy na poprzednika
        prev.right = BSTNode(key, value)
        prev.right.parent = prev

def print_inorder(root, tree):  # rosnąco
    if root is None:
        return
    print_inorder(root.left, tree)
    tree.append(root.key)
    print_inorder(root.right, tree)
    return tree

def remove(root, A, B):
    if root is None:
        return root
    root.left = remove(root.left, A, B)    # przechodizmy drzewo od dołu do góry
    root.right = remove(root.right, A, B)

    if root.key < A:  # jeśli klucz jest mneijszy od lewego kraju zakresu to ustawimy jako root jego prawa gałęź
        root = root.right
    elif root.key > B:  # jeśli klucz jest większy, to zastępujemy root jego lewą gałęzią
        root = root.left
    return root # jesli klucz miesci się w poprawnym zakresie nie trzeba nic robić

if __name__ == '__main__':
    tree = BSTNode(15, 3)
    insert(tree, 10, None)
    insert(tree, 20, None)
    insert(tree, 8, None)
    insert(tree, 12, None)
    insert(tree, 16, None)
    insert(tree, 25, None)
    print(print_inorder(tree, [ ]))
    remove(tree, 9, 12)
    print(print_inorder(tree, [ ]))
    '''        15
             /    \
            /      \
           10       20
          / \      /  \
         /   \    /    \
        8    12 16     25'''
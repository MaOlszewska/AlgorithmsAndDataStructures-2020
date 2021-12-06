''' sprawdzanie czy dane drzewo jest BST czy nie '''


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

def get_min(root):
    prev = None
    while root is not None:
        prev = root    # idac cały czas w lewo dojdziemy do wartosci najmniejszej
        root = root.left
    return prev.key


def get_max(root):
    prev = None
    while root is not None:   # idąc czas czas w prawo dojedziy do wartosci maksymalnej
        prev = root
        root = root.right
    return prev.key

def print_inorder(root, tree):  # rosnąco
    if root is not None:
        print_inorder(root.left, tree)
        tree.append(root.key)
        print_inorder(root.right, tree)
    return tree

def check(root, minimum, maximum):
    if root is None:
        return True

    if root.key < minimum or root.key > maximum:
        return False
    return check(root.left, minimum, root.key) and check(root.right, root.key, maximum )

if __name__ == '__main__':
    tree = BSTNode(15, 3)
    insert(tree, 10, None)
    insert(tree, 20, None)
    insert(tree, 8, None)
    insert(tree, 12, None)
    insert(tree, 16, None)
    insert(tree, 25, None)
    minimum = get_min(tree)
    maximum = get_max(tree)
    print(check(tree, minimum, maximum))
    '''        15
             /    \
            /      \
           10       20
          / \      /  \
         /   \    /    \
        8    12 16     25'''
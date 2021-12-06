''' Mając drzewo Bst, zanjdz parę z sumą o podanej wartości. '''

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


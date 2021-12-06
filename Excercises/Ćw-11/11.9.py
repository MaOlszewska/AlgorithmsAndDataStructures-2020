'''
Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym
zdefiniowanym na węzłach typu:

class BNode:
def __init__( self, value ):
self.left = None
self.right = None
self.parent = None
self.value = val
'''

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

def sumgreater(root, sum):
    if root is None:
        return sum
    right = sumgreater(root.right, sum)
    root.key += right
    sum = root.key
    return sumgreater(root.left, sum)


if __name__ == '__main__':
    tree = BSTNode(5, 3)
    insert(tree, 3, None)
    insert(tree, 8, None)
    insert(tree, 2, None)
    insert(tree, 4, None)
    insert(tree, 6, None)
    insert(tree, 10, None)
    print(print_inorder(tree, [ ]))
    sumgreater(tree, 0)
    print(print_inorder(tree, [ ]))

    '''       5
             /   \
            /     \
           3       8
          / \     / \
         /   \   /   \
        2    4 6     10
    '''
class BSTNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.right = None
        self.left = None


def find(root, key):
    while root is not None:  # dopóki nie zeslzismy na sam dół drzewa przechodizmy po drzweie
        if root.key == key:     # jesli wartość klucza równa się wartosci akturalnego noda to zwracamy aktulany korzeń z znalezonym kluczem
            return root
        elif key > root.key:    # jesśli aktualny klucz jest mniejszy od szukanego to idzimey w prawo
            root = root.right
        else:
            root = root.left    # w innym przypadku idziey w lewo
    return None   # zwracamy none jesli nie znaleźlismy szuaknego klucza


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


def successor(node):                        # szukanie następnika
    x = node
    if x is None:
        return None

    if x.right is not None:                 # jesli ma prawe to następnikiem bedzie wartość najmniejsza z prawego poddrzewa
        return get_min(x.right)

    y = node.parent
    while y is not None and x == y.right:   # wędrujemy w góre drzewa po prawych gałęziach jesli przyszlismy z lewaj krawędzi to znaczy ze znaleźlismzy następnika
        x = y                               # zapamiętujemy poprzedni
        y = y.parent                        # przechodizmy w góre
    if y is None:
        return None
    return y.key


def predecessor(node):                      # szukanie poprzednika
    x = node
    if x is None:
        return None

    if x.left is not None:                  # jesli ma lewe dziecko to następnikiem bedzie wartość najmniejsza z prawego poddrzewa
        return get_max(x.left)

    y = x.parent
    while y is not None and x == y.left:    # sprawdzamy czy nie doslzismy do korzenia drzewa, wędrujemy w góre całe czas jeśli przychodzislmy z prawej strony
        x = y                               # jelsi przysliszmy z lewej storny to mamy poprzednika
        y = y.parent
    if y is None:
        return None
    return y.key


def remove(root, key):
    to_remove = find(root, key)
    if to_remove is None:
        return

    elif to_remove.right is None:   # usuwny liść
        if to_remove.left is None:
            p = to_remove.parent
            if p.left is not None and p.left.key == key:
                p.left = None   # lewe dziecko to liść
            else:
                p.right = None    # prawe dziecko to liść

        else:   # usuwany ma tylko lewe dziecko, więc sprawdzamy czy był lewym czy prawym dzieckiem rodzica
            if to_remove.parent.left is not None and to_remove.parent.left.key == to_remove.key:
                to_remove.parent.left = to_remove.left
            elif to_remove.parent.right is not None and to_remove.parent.right.key == to_remove.key:
                to_remove.parent.right = to_remove.left
    # usuwany ma tylko prawe dziecko i sprawdzamy czy był lewym czy prawym dzieckiem jego rodzica ( analogicznie )
    elif to_remove.left is None:
        if to_remove.parent.left is not None and to_remove.parent.left.key == to_remove.key:
            to_remove.parent.left = to_remove.right

        elif to_remove.parent.right is not None and to_remove.parent.right.key == to_remove.key:
            to_remove.parent.right = to_remove.right

    else:  # usuwany ma dwójke dzieci, wiec szukamy następnika
        succ = successor(to_remove)  # i jego wartosć przepisujemy na usuwanego, poźniej go usuwamy z jego miesjca
        remove(root, succ)
        to_remove.key = succ


def print_inorder(root, tree):  # rosnąco
    if root is not None:
        print_inorder(root.left, tree)
        tree.append(root.key)
        print_inorder(root.right, tree)
    return tree


def print_preorder(root, tree):    # przejscie wzdlużne, najpierw odwiedzamy korzeń poddrzewa,
    if root is not None:     # a następnie przechodzimy kolejno lewe i prawe poddrzewo
        tree.append(root.key)
        print_preorder(root.left, tree)
        print_preorder(root.right, tree)
    return tree


def print_postorder(root, tree):     # przejście wsteczne  najpierw przechodzimy lewe poddrzewo, następnie prawe,
    if root is not None:             # a dopiero na końcu przetwarzamy węzeł.
        print_postorder(root.left, tree)
        print_postorder(root.right, tree)
        tree.append(root.key)
    return tree


if __name__ == '__main__':
    tree = BSTNode(10, 3)
    insert(tree, 5, None)
    insert(tree, 1, None)
    insert(tree, 7, None)
    insert(tree, 40, None)
    insert(tree, 50, None)
    insert(tree, 2, None)
    insert(tree, 8, None)
    insert(tree, 15, None)
    print(print_postorder(tree, []))
    remove(tree, 2)
    print(print_postorder(tree, []))

       #          10
       #        /    \
       #       5     40
       #     /  \    / \
       #    1    7  15  50
       #     \    \
       #      2    8



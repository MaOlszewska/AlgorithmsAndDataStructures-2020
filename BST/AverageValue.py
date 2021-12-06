'''
Zaimplementować funkcję, która oblicza średnią wartość w drzewie BST.
'''

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None

def insert(root,key,value):
    prev=None
    while root is not None :
        if key > root.key :
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left

    if key < prev.key :
        prev.left=Node(key,value)
        prev.left.parent=prev
    else:
        prev.right=Node(key,value)
        prev.right.parent=prev

Sum=0
ctr=0

def inorder(root):
    global Sum      # suma elementów
    global ctr      # licznik elementów
    if root is not None:
        inorder(root.left)
        Sum+=root.key
        ctr+=1
        inorder(root.right)
    return Sum,ctr

def average(root):
    Sum,ctr=inorder(root)
    return Sum

def sumTree(root):
    if root == None:
        return 0

    leftSubTreeSum  = sumTree( root.left )
    rightSubTreeSum = sumTree( root.right )
    mySum = root.key + leftSubTreeSum + rightSubTreeSum;
    return mySum

def find(root, key):
    while root is not None:  # dopóki nie zeslzismy na sam dół drzewa przechodizmy po drzweie
        if root.key == key:     # jesli wartość klucza równa się wartosci akturalnego noda to zwracamy aktulany korzeń z znalezonym kluczem
            return root
        elif key > root.key:    # jesśli aktualny klucz jest mniejszy od szukanego to idzimey w prawo
            root = root.right
        else:
            root = root.left    # w innym przypadku idziey w lewo
    return None   # zwracamy none jesli nie znaleźlismy szuaknego klucza


def get_min(root):
    prev = None
    while root is not None:
        prev = root    # idac cały czas w lewo dojdziemy do wartosci najmniejszej
        root = root.left
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


def remove(root, key):
    toRemove = find(root, key)
    # case 1 node bez dzieci
    if toRemove.left == None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left != None and rodzic.left.key == toRemove.key:
            rodzic.left = None
        else:
            rodzic.right = None

    # case 2 node z prawym dzieckiem
    elif toRemove.left == None and toRemove.right != None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.right
        else:
            rodzic.right = toRemove.right

    # case 3 node z lewym dzieckikem
    elif toRemove.left != None and toRemove.right == None:
        rodzic = toRemove.parent
        if rodzic.left.key == toRemove.key:
            rodzic.left = toRemove.left
        else:
            rodzic.right = toRemove.left

    else:
        # case 4 node posiadajacy oboje dzieci
        toSwitch = succesor(root, toRemove.key)
        tmpKey = toSwitch.key
        remove(root, tmpKey)
        toRemove.key = tmpKey

tree = Node(10, 3)
insert(tree, 5, None)
insert(tree, 1, None)
insert(tree, 7, None)
insert(tree, 40, None)
insert(tree, 50, None)
insert(tree, 2, None)
insert(tree, 8, None)
insert(tree, 15, None)
remove(tree, 8)
print(average(tree))
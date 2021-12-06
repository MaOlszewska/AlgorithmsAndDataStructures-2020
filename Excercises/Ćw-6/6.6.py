'''
Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma—
potencjalnie ujemną—wartość value(v). Proszę zaproponować algorytm, który znajduje wartość najbardziej
wartościowej ścieżki w drzewie T.
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None
        self.path = 0

def val_path(root):
    if root is None:
        return 0, 0

    left, left_best = val_path(root.left)
    right, right_best = val_path(root.right)
    root.path = max(root.val, root.val + left, root.val + right)
    best_path = max(root.path, left_best, right_best)
    return root.path, best_path

if __name__ == '__main__':
    root = Node(5)
    a,b,c,d,e,f = Node(-1), Node(-3), Node(-2), Node(2), Node(3), Node(10)
    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    print(val_path(root)[1])